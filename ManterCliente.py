import streamlit as st
import pandas as pd
from view import View
import time

class ManterClienteUI:
  def main():
    st.header("Cadastro de Clientes")
    tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
    with tab1: ManterClienteUI.listar()
    with tab2: ManterClienteUI.inserir()
    with tab3: ManterClienteUI.atualizar()
    with tab4: ManterClienteUI.excluir()

  def listar():
    clientes = View.cliente_listar()
    if len(clientes) == 0:
      st.write("Nenhum cliente cadastrado")
    else:
      dic = []
      for obj in clientes: 
        for cliente in clientes:
         id = cliente.get_id()
         nome = cliente.get_nome()
         email = cliente.get_email()
         fone = cliente.get_fone()
         senha = cliente.get_senha()
         dic.append([id, nome, email, fone, senha])

      df = pd.DataFrame(dic, columns=["id", "Nome", "E-mail", "Fone","senha"])
      st.dataframe(df)

  def inserir():
    nome = st.text_input("Informe o nome")
    email = st.text_input("Informe o e-mail")
    fone = st.text_input("Informe o fone")
    senha = st.text_input("Informe a senha")
    if st.button("Inserir"):
      if View.cliente_inserir(nome, email, fone, senha) == False:
        st.error("Email já cadastrado")        
      else:
        st.success("Cliente inserido com sucesso")
        time.sleep(2)
        st.rerun()



  def atualizar():
    clientes = View.cliente_listar()
    if len(clientes) == 0:
      st.write("Nenhum cliente cadastrado")
    else:
      op = st.selectbox("Atualização de Clientes", clientes)
      nome = st.text_input("Informe o novo nome", op.get_nome())
      email = st.text_input("Informe o novo e-mail", op.get_email())
      fone = st.text_input("Informe o novo fone", op.get_fone())
      senha = st.text_input("Informe a nova senha", op.get_senha())
      if st.button("Atualizar"):
        if View.cliente_atualizar == True:
          id = op.get_id()
          if View.cliente_atualizar(id, nome, email, fone, senha) == False:
            st.error("Email já cadastrado")        
          else:
            st.success("Cliente inserido com sucesso")
            time.sleep(2)
            st.rerun()
  def excluir():
    clientes = View.cliente_listar()
    if len(clientes) == 0:
      st.write("Nenhum cliente cadastrado")
    else:
      op = st.selectbox("Exclusão de Clientes", clientes)
      if st.button("Excluir"):
        id = op.get_id()
        View.cliente_excluir(id)
        st.success("Cliente excluído com sucesso")
        time.sleep(2)
        st.rerun()
