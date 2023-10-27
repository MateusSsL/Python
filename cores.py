# Códigos ANSI para cores e estilo
RESET = "\033[0m"
BOLD = "\033[1m"
UNDERLINE = "\033[4m"

# Cores de texto
BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

# Cores de fundo
BG_BLACK = "\033[40m"
BG_RED = "\033[41m"
BG_GREEN = "\033[42m"
BG_YELLOW = "\033[43m"
BG_BLUE = "\033[44m"
BG_MAGENTA = "\033[45m"
BG_CYAN = "\033[46m"
BG_WHITE = "\033[47m"

# Exemplo de uso:
('\033[31mERRO! Digite um número inteiro válido.\033[0ml')
# print(f"{RED}Texto em vermelho{RESET}")
# print(f"{BOLD}{BLUE}Texto em azul e negrito{RESET}")
# print(f"{BG_YELLOW}{BLACK}Texto com fundo amarelo e texto preto{RESET}")
