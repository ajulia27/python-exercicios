senha _correta = 123456
nome = "Ana Julia"
tentativa = 3 


     while tentativa > 0:
     senha_digitada += int(input("digite sua senha"))
     if  senha_digitada == senha_correta:
         print(f"ola (nome). seja bem vindo ao nosso banco")
         break   
       else:
         tentativa -= 1
         if tentativa > 0:
             print(f" senha incorreta! vocé ainda tem (tentativa) tentativas.")
         else:
              print(f"(nome), sua senha foi bloqueada! por favor, dirija-se a um dos nossos caixas.")
              break