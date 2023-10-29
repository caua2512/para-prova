from templates.ManterClienteUI import ManterClienteUI
from templates.ManterServicoUI import ManterServicoUI
from templates.ManterAgendaUI import ManterAgendaUI
from templates.AbrirAgendaUI import AbrirAgendaUI
from templates.CadastroUI import CadastroUI

import streamlit as st

class IndexUI:
      
    def sidebar():
      op = st.sidebar.selectbox("Menu", ["Manter Clientes", "Manter Serviços", "Manter Agenda", "Abrir Agenda do Dia", "Clientes"])
      if op == "Manter Clientes": ManterClienteUI.main()
      if op == "Manter Serviços": ManterServicoUI.main()
      if op == "Manter Agenda": ManterAgendaUI.main()
      if op == "Abrir Agenda do Dia": AbrirAgendaUI.main()
      if op == "Clientes": CadastroUI.main()

      #if op == "Manter Clientes": st.session_state["page"] = "manter_clienteUI"

    def main():
      IndexUI.sidebar()

      #if "page" not in st.session_state: st.session_state["page"] = "equacaoUI"
      #if st.session_state["page"] == "manter_clienteUI": ManterClienteUI.main()

IndexUI.main()
