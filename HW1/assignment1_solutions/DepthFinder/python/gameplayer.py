def playgame_dc(gb, left, right):
    if (left == right):
        return left
    if (left == right-1):
        if (gb.ping(left) >= gb.ping(right)):
            return left
        return right

    mid = (left + right) // 2
    if (mid == right):
        return right

    midPing = gb.ping(mid)
    midMinus1Ping = gb.ping(mid-1)
    if (midPing > midMinus1Ping and midPing > gb.ping(mid+1)):
        return mid

    elif (midPing > midMinus1Ping):
        return playgame_dc(gb, mid, right)
    else:
        return playgame_dc(gb, left, mid+1)



