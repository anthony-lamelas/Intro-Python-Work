sun = 5
moon = 7
star = 3
planet = 2
comet = 4
galaxy = 6
nebula = 8
void = False
telegraph = 1
cosmos = True


print(telegraph ** comet + planet *2)
print(nebula + galaxy % star * sun - planet)
print(galaxy // (moon-star) * star)

num4 = (comet*(moon-star) >= 15) or cosomos
print(num4)

num5 = star * sun == moon + galaxy or void and cosmos
print(num5)

num6 = star == nebula // (sun + comet - galaxy) and not void
print(num6)

print(galaxy / planet * telegraph - "void")