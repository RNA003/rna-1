def hni(n,start,target,help):

    if n==1:
        print(f"take disk1 from {start}to {target}")
        return
    hni(n-1,start,help,target)
    print(f"take {n} from {start}to {target}")
    hni(n-1,help,target,start)