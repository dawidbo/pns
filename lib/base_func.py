def getSec():
    """
        get from file data for settings.py file
        return { dictionary } with conf file
    """
    ans = []
    ansDict = {}
    fname = '../../settingsPns.txt'

    with open(fname) as file:
        content = file.readlines()

    for line_elt in content:
        ans = line_elt.split("===")
        if len(ans) == 2:
            key = ans[0].strip()
            value = ans[1].strip()
            assert not(" " in key or " " in value), "Spaces in config file!"
            ansDict[key] = value
        else:
            assert False, "Config file has been write in wrong format!"

    return ansDict