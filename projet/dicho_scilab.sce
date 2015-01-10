function [rc]=myFunction(x)
    rc=cos(x)-x
    return rc
endfunction

function [rc]=dichotomie(a, b, epsilon)
    extg = a
    extd = b
    compteur = 0
    while abs(extd-extg)>epsilon
        compteur = compteur +1
        milieu = (extd+extg)/2
        fmilieu = myFunction(milieu)
        if myFunction(extg)*fmilieu>0 then
            extg = milieu
            extd = extd
        else
            extg = extg
            extd = milieu
        end
    end
    rc = [extg, extd, compteur]
    return rc
endfunction

function [rc]=factorielle(n)
    rc = 1
    for j= 1:n
        rc = rc * j
    end
    return rc
endfunction
