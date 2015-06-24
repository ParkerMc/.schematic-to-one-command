def to_cmd(commands):
    output = "summon MinecartCommandBlock ~ ~1 ~ {Riding:"
    for i in commands:
        output = output + "{id:MinecartCommandBlock,Riding:"
    output = output + "{id:FallingSand,TileID:157,Time:1}"
    for i in commands:
        output = output + ",Command:"+i+"}"
    output = output + ",Command:setblock ~ ~ ~ lava 7}"
    print output

