if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for i in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
        i+=1
    query = raw_input()
    avg=sum(student_marks[query])/3
    print "%.2f" % avg
