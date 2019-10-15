
def string_match(src, key):
    return [ name for name in src if key in name]












src = {"minecraftgame", "intelligent", "innercrafttalent", "knife", "scissor", "stonecrafter"}
key = "craft"


print(string_match(src, key))



