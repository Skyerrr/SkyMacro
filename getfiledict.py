



def getmaclist():
    global script_name
    script_name = {}
    try:
        with open("macro_file.txt", "r") as fi:
            for ln in fi:
                if ln.startswith("["):
                    name = ln[1:-2]
                    script_name[ln[1:-2]] = []
                if ln.startswith("bindedkey="):
                    script_name[name].append(ln[:-1])

                if ln.startswith("e={"):
                    script_name[name].append(ln[3:-2])

                if ln.startswith("d="):
                    delay = ln.split("d=")
                    script_name[name].append(delay[1][:-1])
        return script_name
    except:
        script_name = {}
        script_name["Example1"] = ["bindedkey=72", "q down", "0.030", "q up"]
        script_name["Example2"] = ["bindedkey=71", "q down", "0.030", "q up"]
        with open("macro_file.txt", "w") as fi:
            for k, v in script_name.items():
                if k:
                    fi.write(str(f"[{k}]" + "\n"))
                if v:
                    for item in v:
                        if item.startswith("bindedkey="):
                            fi.write(item + "\n")
                        if item.replace('.', '', 1).isdigit():
                            fi.write(f"d={item}" + "\n")
                        if not item.startswith("bindedkey=") and not item.replace('.', '', 1).isdigit():
                            fi.write("e={" + f"{item}" + "}" + "\n")
        getmaclist()












