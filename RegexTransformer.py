import re

def Templates2Regex(template):
    regex = template
    regex = regex.replace("\\", "\\\\")
    regex = regex.replace(".", "\.")
    regex = regex.replace("*", "\*")

    regex = regex.replace("<\*>", ".*")

    regex = regex.replace("(", "\(")
    regex = regex.replace(")", "\)")

    regex = regex.replace("[","\[")
    regex = regex.replace("]","\]")
    return regex

def RegexMatch(tmp_list, file):
    num_match = 0

    logfile = open(file)
    loglines = logfile.readlines()

    matchlist = []

    for tmp_ori in tmp_list:
        tmp = Templates2Regex(tmp_ori)
        index = 0

        for line in loglines:
            if (index in matchlist):
                pass
            else:
                match = re.search(tmp, line)
                if match:
                    num_match = num_match+1
                    matchlist.append(index)
                else:
                    pass
            index = index + 1
            print(index)

    index = 0
    unmatchedlogs = []
    unmatchedindex = []
    for line in loglines:
        if(index in matchlist):
            pass
        else:
            unmatchedindex.append(index)
            unmatchedlogs.append(line)
        index = index + 1

    print(num_match)
    return unmatchedlogs