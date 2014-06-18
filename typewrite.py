def typewrite(string, length=0.075):
        import sys, time
        for i in string:
                sys.stdout.write(i)
                sys.stdout.flush()
                time.sleep(length)
