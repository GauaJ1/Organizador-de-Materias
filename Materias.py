Materias = str(input('Defina uma nova matéria: '))


if __name__ == '__main__':
    print(Materias)
    from time import sleep
    from tqdm import tqdm
    Barra = tqdm(total=200)
    for i in range(200):
        sleep(0.005)
        Barra.update(1)
    Barra.close()
    Del = input('''Quer \033[1;31mDeletar\033[m o Arquivo? (s/n)
    ''')
    if Del == 's':
        def ResetGeral(file_path):
    
            with open(file_path, 'w'):
                pass
        ResetGeral('Materias.Txt')
        exit()
    else:
        pass
        
    print(f'Oque Deseja Escrever em {Materias}? ')
    R = input(''' ''')
with open('Materias.txt', 'a') as file:
    file.write('Materia:')
with open('Materias.txt', 'a') as file:
    file.write(Materias)
with open('Materias.txt', 'a') as file:
    file.write('''
    
    ''')
with open('Materias.txt', 'a') as file:
    file.write(R)
with open('Materias.txt', 'a') as file:
    file.write('''
    
    
    ''')
print('\033[1;32mSalvo com Sucesso!\033[m')

    