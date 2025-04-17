def main():
    name=input(f'Enter your name: ')
    print(f'Your name is {name.title()}. \n Your initials: {initials(name)}')
    initials(name)

def initials(name_local):
    parts=(name_local.strip().split())
    initial=[]
    for chunks in parts:
        initial.append(chunks[0].upper())
    ini="".join(initial)
    return ini


if __name__=='__main__':
    main()
