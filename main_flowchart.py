import sys
from graphviz import Digraph
from plyparser import create_new_parser, testToken
from plyparser import error_logger
import os

def draw_flowchart(source_code):
    print("\n")
    error_logger.clear()

    lexer = testToken(source_code)
    print("------------------------------------end of lexer part--------------------------------------------")
    parser = create_new_parser()
    result = parser.parse(source_code)

    if(len(error_logger) != 0):
        print("error (main_flowchart.py)", error_logger)
        return error_logger

    print("\n")
    print("result ", result, "\n")

    final_res = []
    closing_code = []

    def convert(p):
        print("p", p, "\n")
        if (isinstance(p, tuple)):
            size = len(p)

            if (size == 3 or size == 4 and p[-1] != '}'):
                
                final_res.append(p[0:])
            else:
                
                final_res.append(p[0:3])

                for i in range(3, len(p)):
                    print("p[i]", p[i])
                    if (p[i] != '}'):
                        convert(p[i])
                    else:
                        final_res.append('}')

        elif (isinstance(p, list)):
            for a in p:
                convert(a)
        else:
            final_res.append(p)

    convert(result)
    print("final_res", final_res)

    def set_label(data):
        res = ''
        for i in data:
            res += str(i) + "."
        return res

    line = 1  
    scope = [0]  
    position = 0  
    new_indexing_result = []
    for i in final_res:
        data = i
        if(isinstance(i, tuple)):
            data = list(i)

        size = len(data)
        scope[position] += 1
        print("scope", scope)

        # print("data", data, size)
        label = set_label(scope[0:position + 1])
        if (data[-1] == '}'):
            scope[position] = 1
            position -= 1

            label = set_label(scope[0:position + 1])
            scope[position+1] = 0

        if (data[-1] == '{' or data[0]=='else'):
            scope.append(0)
            position += 1

        if (isinstance(i, tuple)):
            data.insert(0, label)
            new_indexing_result.append(data)
        else:
            new_indexing_result.append([label, i])

    print("scope", scope)

    for i in new_indexing_result:
        print("#", i)
    new_indexing_result2 = []
    for i in new_indexing_result:
        if i[1] == '}':
            continue
        else:
            new_indexing_result2.append(i)

    fc = Digraph(name="flowchart", strict=True, format='png')

    num = 0

    scope2 = []
    for i in new_indexing_result:
        scope2.append(i[0])

    source = []
    target = []

    last_statement_num = 0
    end_found = False

    def get_num(indexing):
        for i in range(0, len(new_indexing_result2)):
            if (new_indexing_result2[i][0] == indexing):
                return i
        return -1

    for i in new_indexing_result:
        if i[1] in {'int', 'string', 'bool', 'char', 'float'}:
            fc.node(str(num), label=i[1]+' '+i[2], shape='rectangle', style='filled', color='#a29bfe')
            if num == 0:
                fc.attr('node', rankdir='LR')
                fc.node('start', shape='oval', style='filled', color='#55efc4')
                fc.edge('start', str(num))
            if num > 0:
                # check nunjuk arrownya mesti sesama sibling
                current_array = str(new_indexing_result2[num - 1][0]).split('.')
                current = current_array[0:len(current_array) - 2]

                dest_array = str(new_indexing_result2[num][0]).split('.')
                dest = dest_array[0:len(dest_array) - 2]
                print(current, " :: ", dest)
                if (current == dest):
                    fc.edge(str(num - 1), str(num))

            num += 1

            if scope2[num - 1] == scope2[-1] and end_found == False:
                fc.node(str(num), label='end', shape='oval', style='filled', color='#55efc4')
                fc.edge(str(num - 1), str(num))
                end_found = True

            last_statement_num = num

        if i[1] in {'while', 'for', 'if', 'ELSE IF'}:
            fc.attr('node', shape='diamond')

            if i[1] in {'while', 'for'}:
                if i[1] == 'for':
                    # Special handling for for loops
                    condition_text = i[2][2]
                else:
                    condition_text = i[2][2]
                fc.node(str(num), label=condition_text, shape='diamond', style='filled', color='#fdcb6e')
            else:
                fc.node(str(num), label=i[2][2], shape='diamond', style='filled', color='#3498db')

            if num > 0:
                fc.edge(str(num - 1), str(num))
            if num == 0:
                fc.attr('node', rankdir='LR')
                fc.node('start', shape='oval', style='filled', color='#55efc4')
                fc.edge('start', str(num))
            num += 1

            a = int(i[0][-2])

            if len(i[0]) > 2:
                if i[0][-2] == str(a):
                    for s in range(0, len(new_indexing_result2)):
                        if i[0][0:-2] + str(a + 1) + '.' in scope2:
                            if i[0][0:-2] + str(a + 1) + '.' == new_indexing_result2[s][0]:
                                fc.edge(str(num - 1), str(s), label='false')
                                break
                        elif i[0][0:-2] + str(a + 1) + '.' not in scope2:
                            for j in range(num - 2, -1, -1):
                                if new_indexing_result2[j][1] in {'while', 'for'}:
                                    str_index = i[0]
                                    while str_index != '':
                                        str_index = str_index[0:-2]
                                        if str_index == new_indexing_result2[j][0]:
                                            fc.edge(str(num - 1), str(j), label='false')
                                            break
                                    break
                                else:
                                    for k in range(num, len(new_indexing_result2)):
                                        if new_indexing_result2[k][1] in {'while', 'for'}:
                                            fc.edge(str(num - 1), str(k), label='false')
                                            break
            elif len(i[0]) == 2:
                deststr = str(int(i[0][0:-1]) + 1) + '.'
                dest = str(get_num(deststr))
                if (dest != '-1'):
                    print("robert : ", i[0], "to : ", dest)
                    fc.edge(str(num - 1), dest, label='false')

            if i[0] == new_indexing_result[len(new_indexing_result) - 1][0] and end_found == False:
                fc.node('end', shape='oval', style='filled', color='#55efc4')
                fc.edge(str(num - 1), 'end', label='false')
                end_found = True
            elif scope2[num - 1][-2] != '1':
                fc.edge(str(num - 1), str(num))

            fc.edge(str(num - 1), str(num), label='true')
            last_statement_num = num

        if i[1] in {'cin', 'cout'}:
            fc.attr('node', shape='parallelogram', style='filled', color='#fab1a0')
            fc.node(str(num), label='print ' + i[3])

            if num > 0:
                fc.node(str(num), label='print ' + i[3], shape='parallelogram', style='filled', color='#fab1a0')

                # check nunjuk arrownya mesti sesama sibling
                current = new_indexing_result2[num - 1][0][0:-2]
                dest = new_indexing_result2[num][0][0:-2]
                if (current == dest):
                    fc.edge(str(num - 1), str(num))
            if num == 0:
                fc.attr('node', rankdir='LR')
                fc.node('start', shape='oval', style='filled', color='#55efc4')
                fc.edge('start', str(num))

            num += 1
            last_statement_num = num

    # Get all edges in the flowchart
    k = fc.body
    list_arrow = []
    for i in k:
        if '->' in i:
            list_arrow.append(i)

    source = []
    end = []
    for i in list_arrow:
        data = i.split('->')
        source.append(str.rstrip(str(data[0]).replace('\t', '')))
        end.append(str.rstrip(str(data[1]).split(' ')[1]))

    # Add back edges for loops
    for i in new_indexing_result2:
        indexing = i[0]
        if (len(indexing) > 2):
            new_indexing = indexing[0:-2] + str(int(indexing[-2][-1]) + 1) + '.'
            pos = get_num(new_indexing)
            
            if (pos == -1):
                s = str(get_num(indexing))
                dest = str(get_num(str(new_indexing_result2[int(s)][0][0:-2])))
                next = int(s) + 1
                str_indexing = str(indexing)

                current_array = str_indexing.split('.')

                try:
                    # Check next siblings of previous scope/parent exist or not
                    next_str_indexing = current_array[0:len(current_array) - 2]
                    next_str_indexing = str.join('.', next_str_indexing[0:-1]) + '.' + str(
                        int(next_str_indexing[-1]) + 1) + '.'
                    
                    found = False
                    if (get_num(next_str_indexing) == -1):
                        while (str_indexing != ''):
                            str_indexing = str_indexing[0:-2]
                            if str_indexing and get_num(str_indexing) != -1 and new_indexing_result2[get_num(str_indexing)][1] in {'while', 'for'}:
                                fc.edge(s, str(get_num(str_indexing)))
                                found = True
                                break
                except:
                    print("enter catch")

                if not found:
                    if (str(next) in end):
                        fc.edge(s, str(next))
                        found = True
                    elif (str(next) not in end and end_found == False):
                        fc.edge(s, 'end')
                    else:
                        if (str(next) in end):
                            fc.edge(s, str(next))
                        else:
                            if new_indexing_result2[int(s)][1] in {'if', 'while', 'for', 'ELSE IF', 'else'}:
                                fc.edge(s, 'end', label='false')
                            else:
                                fc.edge(s, 'end')

                if int(dest) < len(new_indexing_result2) and new_indexing_result2[int(dest)][1] in {'while', 'for'}:
                    fc.edge(s, dest)

    # Add final end node if needed
    k = fc.body
    list_arrow = []
    for i in k:
        if '->' in i:
            list_arrow.append(i)

    source = []
    end = []
    for i in list_arrow:
        data = i.split('->')
        source.append(str.rstrip(str(data[0]).replace('\t', '')))
        end.append(str.rstrip(str(data[1]).split(' ')[1]))

    if 'end' not in end and end_found == False:
        fc.node('1000', label='end', shape='oval', style='filled', color='#55efc4')
        fc.edge(str(last_statement_num - 1), '1000')
        end_found = True

    fc.view()
    return None  # Return None means no errors