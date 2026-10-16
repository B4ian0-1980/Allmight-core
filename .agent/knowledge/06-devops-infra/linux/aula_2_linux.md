---json
{
  "id": "aula_2_linux",
  "title": "Aula 2 Linux",
  "categoria": "06-devops-infra",
  "subcategoria": "linux",
  "resumo": "Guia tecnico e referencias sobre Aula 2 Linux.",
  "gatilhos": [
    "aula",
    "devops",
    "infra",
    "linux"
  ],
  "perguntas_tipo": [
    "Como utilizar Aula 2 Linux?",
    "Quais as boas praticas de linux?"
  ],
  "nao_cobre": [],
  "target_agent": [
    "general-assistant"
  ],
  "source": {
    "origin": "AllMight Knowledge Base",
    "original_format": "markdown"
  },
  "atualizado_em": "2026-10-15",
  "verificado_em": "2026-10-15",
  "dono": "stack-linux",
  "prioridade": 2
}
---

**MARATONA PROFISSIONAIS LINUX**** **

**#  **

Link da aula: ​https://sl.profissionaislinux.com/aula-2-maratona-fpl1/tutorial-secreto-2/ 

**#  **

**# Decifrando de uma vez por todas a **

**# estrutura do sistema **# ​**# GNU/LINUX**#  


**# / – diretório raiz **

** **
Tudo o que está no seu sistema Linux fica localizado neste diretório, conhecido 
como diretório raiz. 
Ele pode ser considerado o diretório C:\ do Windows. 
Entretanto, isso não é rigorosamente verdade, porque o Linux não têm letras de 
unidades. 
Enquanto outra partição no Windows ficará localizada em D:\, no sistema Linux 
essa partição irá aparecer em uma pasta dentro do diretório raiz. 
 ( ponto de montagem ) 
** **

***Por Pedro Delfino - ***​***Profissionais Linux***​***  - Página: 1 ***


--------------------------------------------------

**MARATONA PROFISSIONAIS LINUX**** **

**# /boot – arquivos do processo de inicialização **

O diretório /boot contém os arquivos necessários para inicializar o sistema. Por 
exemplo, os arquivos GRUB e seus kernels Linux são armazenados aqui. 

**# /bin – binários essenciais **

O diretório /bin contém os comandos binários essenciais (programas) que devem estar 
presentes quando o sistema é montado. 
Os aplicativos são armazenados em /usr/bin, enquanto os programas importantes do 
sistema e utilitários, como o shell bash, ficam localizados em /bin. 
O diretório /usr pode ser armazenado em outra partição. 
Por isso, colocar esses arquivos no diretório /bin garante que o sistema terá os programas 
mais importantes, mesmo se não houver outros sistemas de arquivos montados. 
O diretório /sbin é semelhante,​ pois ele contém os arquivos binários para​ a administração 
do sistema. 

**# /etc – arquivos de configuração **

O diretório /etc contém arquivos de configuração, que geralmente podem ser editados 
à mão em um editor de texto. 
Observe que o diretório /etc contém arquivos de todo o sistema de configuração. 

**# /dev – arquivos de dispositivos **

O Linux considera dispositivos como arquivos, e o diretório /dev contém uma série de 
arquivos especiais que representam os dispositivos. Esses não são arquivos reais 
como nós conhecemos, mas eles aparecem como arquivos. 
Por exemplo /dev/sda representa a primeira unidade SATA no sistema. Se você quiser 
particioná-lo, deverá informar em um programa específico para editar o arquivo 
/dev/sda. 
Esse diretório contém pseudo dispositivos, que são dispositivos virtuais que na 
verdade não correspondem ao hardware. Por exemplo: /dev/random gera números 
aleatórios. 

***Por Pedro Delfino - ***​***Profissionais Linux***​***  - Página: 2 ***


--------------------------------------------------

**MARATONA PROFISSIONAIS LINUX**** **


**# /home – pastas pessoais **

O diretório /home contém uma pasta base para cada usuário. Por exemplo, se seu nome 
de usuário é Pedro, você tem uma pasta base localizado em /home/pedro. 
Essa pasta contém os arquivos de dados e arquivos de configuração específicos do 
usuário. 
Os usuários só têm permissão para gravar dentro de suas próprias pastas e devem obter 
permissões superiores para modificar outros arquivos no sistema. 

**# /lib - Bibliotecas essenciais **

O diretório /lib contém as bibliotecas necessárias para os comandos binários essenciais 
para as pastas /bin e /sbin. 
**As bibliotecas necessárias pelos binários na pasta /usr/bin estão localizadas em **
**/usr/lib** 

**# /lost+found - arquivos recuperado **

Se houverem falhas no sistema de arquivos, uma verificação do sistema será 
realizada na próxima inicialização. 
Qualquer arquivo corrompido encontrado será colocado nesse diretório, de modo 
que você possa tentar recuperar os dados. 

**# /media - mídias removíveis **

O diretório /media contém subdiretórios​ em que os dispositivos de mídia removível 
inserido no computador são montados. 
Por exemplo, quando você insere um CD em seu sistema Linux, um diretório será 
criado automaticamente dentro do diretório /media. 
Você pode acessar o conteúdo do CD dentro desse diretório. 

***Por Pedro Delfino - ***​***Profissionais Linux***​***  - Página: 3 ***


--------------------------------------------------

**MARATONA PROFISSIONAIS LINUX**** **

**# /mnt – montagem de sistemas temporários **

O diretório /mnt é o lugar no qual os administradores de sistema montam sistemas de 
arquivos temporários enquanto os usam. 
Por exemplo, se você estiver montando uma partição do Windows​ para executar 
algumas operações de recuperação de arquivos, você pode montá-lo em 
/mnt/windows. 
No entanto, você pode montar outros sistemas de arquivos em qualquer lugar no 
sistema. 

**# /opt - pacotes opcionais **

O diretório /opt contém subdiretórios para pacotes de software opcionais. 
É usado por softwares proprietários, que não obedecem à hierarquia do sistema de 
arquivos-padrão —​ por exemplo, um programa proprietário ​pode colocar seus 
arquivos em /opt/aplicativo quando você instalá-lo. 

**# /proc – kernel e arquivos de processo **

O diretório /proc é semelhante ao diretório /dev, pois contém arquivos especiais que 
representam sistemas e informações de processo e não contém arquivos padrão 
Contém informações do KERNEL e de processo que estão rodando momento 

**# /root - Diretório home para o super usuário **

O diretório /root é o diretório home para o super usuário do Linux.  
Em vez de estar localizado em /home/root, ele está localizado apenas em /root. 
Isto é diferente do diretório /, que é o diretório raiz do sistema 

**# /run - arquivos temporários de aplicativos **


***Por Pedro Delfino - ***​***Profissionais Linux***​***  - Página: 4 ***


--------------------------------------------------

**MARATONA PROFISSIONAIS LINUX**** **

O diretório /run é relativamente novo, e oferece aos aplicativos um local padrão para 
armazenar arquivos temporários, como soquetes e identificações de processos. 
Esses arquivos não podem ser armazenados em /tmp, pois os arquivos localizados 
em /tmp podem ser apagados. 

**# /srv - serviço de dados **

O diretório /srv contém “dados para serviços prestados pelo sistema”. Se você usa o 
servidor Apache em um site, provavelmente armazena os arquivos do seu site em um 
diretório dentro do /srv 

**# /tmp - arquivos temporários **

Os aplicativos e programas armazenam arquivos temporários no diretório /tmp. 
Esses arquivos geralmente são apagados quando o sistema é reiniciado, sendo que essa 
requisição pode ser revogada a qualquer momento por utilitários como o tmpwatch 

**# /usr - dados somente leitura **

O diretório /usr contém aplicativos e arquivos utilizados pelos usuários, ao contrário 
de aplicativos e arquivos utilizados pelo sistema. 
Por exemplo, aplicativos não essenciais estão localizados dentro do diretório /usr/bin 
em vez do diretório /bin e os arquivos binários não essenciais de administração do 
sistema estão localizados no diretório /usr/sbin em vez do diretório /sbin. 

**# /var - arquivos de dados variáveis **

O diretório /var é a contrapartida gravável para o diretório /usr. 
Os arquivos de log e todos os outros são gravados no diretório /var 

***Por Pedro Delfino - ***​***Profissionais Linux***​***  - Página: 5 ***

