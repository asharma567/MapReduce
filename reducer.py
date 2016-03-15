import sys
import json
import ast



if __name__ == '__main__':
    output_dic = {}
    for line in sys.stdin:
        try:
            cnter_dict = ast.literal_eval(line)
            for key, val in cnter_dict.iteritems():
                if output_dic.get(key):
                    output_dic[key] += 1
                else:
                    output_dic[key] = val

        except:
            print >> sys.stderr, line, len(line)

    encoder_obj = json.encoder.JSONEncoder()
    print encoder_obj.encode(output_dic)
    with open('output_dic.json','wb') as f:
        f.write(encoder_obj.encode(output_dic))
    print 'Saved.'
    