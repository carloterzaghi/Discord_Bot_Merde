from cProfile import label
from tkinter import Button
from nextcord.ext import commands
import nextcord
from nextcord import Interaction
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from nextcord.ui import Button, View
import random
from pergunta import escolher_aleatorio, quantidade1
from pergunta_sexy import escolha_pergunta_sexy, quantidade2
from pergunta_pesada import escolha_pergunta_pesada, quantidade3
from nextcord import ButtonStyle

db = firestore.client()

class PlayGame(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name= "play") #Comando m!play
    async def play(self, ctx):
        lista_foi = [] #Lista das pergunta que já foram
        quantidade_de_pergunta = quantidade1()+quantidade2()+quantidade3() # Quantidade de perguntas que existem 

        print(quantidade_de_pergunta)

        # user = ctx.message.author.id
        # db.collection("games").document().set({
        #         "perguntas" : ['foi'],
        #         "players" : [user],
        # })

        # Botões do m!play
        modo_livre =  Button(label= 'Modo Livre', style= ButtonStyle.green)
        modo_disc =  Button(label= 'Modo Disc', style= ButtonStyle.red)

        async def livre(interaction):
            proximo = Button(label= 'Próximo', style= ButtonStyle.green)
            termina = Button(label= 'Terminar', style= ButtonStyle.red)

            async def next(interaction):
                await livre(interaction)

            async def acaba(interaction):
                embed = nextcord.Embed(
                title = 'Fim de Jogo',
                color = 0x97CBFF
                )   
                proview = View(timeout=240)
                await interaction.response.edit_message(embed = embed,view = proview)

            while True:
                escolher = random.choice([escolher_aleatorio(),escolha_pergunta_sexy(), escolha_pergunta_pesada()])
                if escolher in lista_foi:
                    pass
                elif len(lista_foi) == quantidade_de_pergunta -1:
                    return await acaba(interaction)
                else:
                    lista_foi.append(escolher)
                    break

            proximo.callback = next
            termina.callback = acaba

            proview = View(timeout=240)
            proview.add_item(proximo)
            proview.add_item(termina)

            if 1 in escolher:

                embed = nextcord.Embed(
                    title = escolher[0],
                    color = 0x495A6A
                )   

            elif 2 in escolher:

                embed = nextcord.Embed(
                    title = escolher[0],
                    color = 0xFF33BB
                )  
            
            elif 3 in escolher:

                embed = nextcord.Embed(
                    title = escolher[0],
                    color = 0xED2020
                ) 

            # docs = db.collection('games').get()
            # palavras = []
            # for doc in docs:
            #     if user in doc.to_dict()['players']:
            #         key = doc.id
            #         pegar_user = db.collection('games').document(key).get()
            #         for i in pegar_user.to_dict()["perguntas"]:
            #             palavras.append(i)
            # if escolher[0] in palavras:
            #     await livre(interaction)
            # else:
            #     palavras.append(escolher[0])
            #     for doc in docs:
            #         if user in doc.to_dict()['players']:
            #             key = doc.id
            #             db.collection('games').document(key).update({
            #                 "perguntas" : palavras,
            #             })

            await interaction.response.edit_message(embed = embed, view = proview)
                
        async def disc(interaction):
            embed = nextcord.Embed(
                title = "__Alerta__",
                description = "Este modo ainda está em produção!",
                color = 0x97CBFF
            )   
            await interaction.response.send_message(embed = embed)

        modo_livre.callback = livre
        modo_disc.callback = disc

        myview = View(timeout=180)
        myview.add_item(modo_livre)
        myview.add_item(modo_disc)

        embed = nextcord.Embed(
                title = "__Jogo de Merda__",
                description = "*Para iniciar o jogo selecione um dos modos.*\n⠀",
                color = 0x97CBFF
            )  
        embed.add_field(name= "\n__REGRAS__", value=
             'Alguém puxa uma carta e faz uma pergunta. Todos os outros imediatamente apontam para quem eles acham que “cumpre” perfeitamente os requisitos da pergunta. '+
             'O mais votado ganha! Aquele que ganhar 6 vezes é coroado o **AMIGO DE MERDA!**\n⠀'
             , inline=False) 
        embed.add_field(name= "\n__CARTAS__", value=
             '**Cinza:** Perguntas Normais\n**Rosa:** Perguntas Quentes\n**Vermelho:** Perguntas Pesadas\n⠀'
             , inline=False) 
        embed.add_field(name= "\n__MODO LIVRE__", value=
             'Modo recomendado para jogar fora do Discord com os amigos, com menos comandos e sem pontuação.\n⠀'
             , inline=False)
        embed.add_field(name= "\n__MODO DISC (EM CONSTRUÇÃO)__", value=
             'Modo recomendado para jogar no Discord com os amigos.'
             , inline=False)

        await ctx.send(embed = embed, view = myview)

def setup(bot):
    bot.add_cog(PlayGame(bot))