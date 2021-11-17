def song(a1=3, a2=3, a3=0):
    word = 'la'
    ver1 = (word + '-') * a2
    ver1 = ver1.rstrip('-')
    ver2 = (ver1 + '\n') * a1
    ver2 = ver2.rstrip('\n')
    if a3 == 0:
        out = ver2 + '.'
    else:
        out = ver2 + '!'
    return out


if __name__ == '__main__':
    # 1
    r = song(5, 4, 0)
    f = open('lalala.txt', 'w')
    print(r, file=f)
    f.close()

    f1 = open('lalala.txt')
    for i in f1:
        print(i.rstrip('\n') + '!')
    f1.close()

    f2 = open('d://GitWorkspace/homework/project_5/task1_1_homework5.py')
    all_read = f2.read()
    print(all_read)
    f2.close()

    f3 = open('lalala.txt')
    f4 = open('lalala1.txt', 'w')
    for line in f3:
        print('Number: ' + line.rstrip(), file=f4)
    f3.close()
    f4.close()

    f5 = open('numb.txt')
    try:
        for line in f5:
            line = int(line)
        else:
            print('I did it')
    except ValueError:
        pass
    finally:
        f5.close()

    # 2
    with open('numb.txt') as f6:
        try:
            for line in f6:
                line = int(line)
            else:
                print('I did it')
        except ValueError:
            pass
        finally:
            f6.close()
