# Passo a passo Hashzap

# Passo 1: Botão de iniciar chat
# Passo 2: Popup para entrar no chat
# Passo 3: Quando entrar no chat: (aparece para todo mundo)
  # 3.1: A mensagem que você entrou no chat
  # 3.2: O campo e o botão de enviar mensagem
# Passo 4 A cada mensagem que você envia (aparece para todo mundo)
  # 4.1: Nome: Texto da Mensagem

import flet as ft # 1 

def main(pagina): # 2
  texto = ft.Text("Hashzap")

  chat = ft.Column()

  nome_usuario = ft.TextField(label='Escreva seu nome')

  def enviar_mensagem_tunel(mensagem):
    texto_mensagem = mensagem['texto']
    usuario_mensagem = mensagem['usuario']
    # Adicionar a mensagem no chat
    chat.controls.append(ft.Text(f'{usuario_mensagem}: {texto_mensagem}'))
    pagina.update()

  # PUBSUB -> PUBLISH SUBSCRIBE
  # Túnel de comunicação entre os usuários

  pagina.pubsub.subscribe(enviar_mensagem_tunel)
  
  def enviar_mensagem(evento):
    pagina.pubsub.send_all({'texto': campo_mensagem.value, 'usuario': nome_usuario.value})
    # Limpar o campo de mensagem
    campo_mensagem.value = ""
    pagina.update()


  campo_mensagem = ft.TextField(label='Digite sua mensagem')
  botao_enviar_mensagem = ft.ElevatedButton('Enviar', on_click=enviar_mensagem)

  def entrar_popup(evento):
    # Adicionar o chat
    pagina.add(chat)

    # Fechar o popup
    popup.open = False
    
    # Remover o botão iniciar chat
    pagina.remove(botao_iniciar)
    pagina.remove(texto)

    # Criar o campo de mensagem do usuario
    pagina.add(ft.Row(
      [campo_mensagem, botao_enviar_mensagem]
    ))

    # Criar o botão de enviar mensagem do usuário
    pagina.add(botao_enviar_mensagem)
    pagina.update()

  popup = ft.AlertDialog(
    open=False, 
    modal=True,
    title=ft.Text('Bem vindo ao Hashzap'),
    content=nome_usuario,
    actions=[ft.ElevatedButton('Entrar', on_click=entrar_popup)],
    )
  
  def entrar_chat(evento):
    pagina.dialog = popup
    popup.open = True
    pagina.update()

  botao_iniciar = ft.ElevatedButton('Iniciar chat', on_click=entrar_chat)

  pagina.add(texto)
  pagina.add(botao_iniciar)

ft.app(target=main, view=ft.WEB_BROWSER)
