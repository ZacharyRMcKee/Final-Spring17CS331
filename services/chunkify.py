def chunkify(list,pieces):

    # ex. [1,2,3,4,5,6,7,8,9,10] - > [[1,2,3,4],[5,6,7],[8,9,10]]
    chunkedSize = 0
    out = []
    if pieces <= len(list):
        for i in range(pieces-1):
            out.append(list[chunkedSize:(chunkedSize+len(list)//pieces)])
            chunkedSize += len(list)//pieces
        out.append(list[chunkedSize:])
    else:
        return [list] # The list is so small that we do not care about splitting it up in this case.
    return out