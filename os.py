import os
'''
cwd = os.getcwd()


print('Directorio de trabajo actual', cwd)
'''

txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]
print('Los archivos txt son', txt_files)


os.rename('cuento.txt','cuento2.txt')


txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]
print('Los archivos txt son', txt_files)
