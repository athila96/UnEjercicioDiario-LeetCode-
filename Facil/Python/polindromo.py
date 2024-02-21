class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False

        original = x
        invertido = 0

        while x > 0:
            digito = x % 10
            invertido = invertido * 10 + digito
            x //= 10

        return original == invertido

solucion = Solution()
numero = 121

if solucion.isPalindrome(numero):
    print(f"{numero} es un palindromo")
else:
    print(f"{numero} no es un palindromo")

        