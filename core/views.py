from django.shortcuts import render
import random
from django.views.decorators.http import require_http_methods
FRUTAS = {
    "morango": {
        "nome": "Morango",
        "emoji": "🍓",
        "perfil": "Você é carismático, sociável e simpático. Seu jeito divertido aproxima as pessoas!",
    },
    "abacaxi": {
        "nome": "Abacaxi",
        "emoji": "🍍",
        "perfil": "Você é aventureiro, corajoso e cheio de atitude. Gosta de desafios e novidades!",
    },
    "melancia": {
        "nome": "Melancia",
        "emoji": "🍉",
        "perfil": "Você é tranquilo, leal e companheiro. As pessoas encontram conforto na sua presença!",
    },
    "laranja": {
        "nome": "Laranja",
        "emoji": "🍊",
        "perfil": "Você é otimista, animado e cheio de energia. Sempre encontra motivos para seguir em frente!",
    },
    "banana": {
        "nome": "Banana",
        "emoji": "🍌",
        "perfil": "Você é descontraído, divertido e espontâneo. Seu bom humor torna os momentos especiais!",
    },
    "uva": {
        "nome": "Uva",
        "emoji": "🍇",
        "perfil": "Você é criativo, sensível e cheio de imaginação. Enxerga possibilidades onde outros não veem!",
    },
    "maca": {
        "nome": "Maçã",
        "emoji": "🍎",
        "perfil": "Você é organizado, responsável e dedicado. Gosta de fazer as coisas com atenção!",
    },
    "manga": {
        "nome": "Manga",
        "emoji": "🥭",
        "perfil": "Você é curioso, espontâneo e aberto a novidades. Adora descobrir coisas diferentes!",
    },
}

PERGUNTAS = [
    {
        "id": 1,
        "texto": "Como você prefere passar o fim de semana?",
        "alternativas": [
            {"valor": "A", "texto": "Saindo com os amigos e dando risada."},
            {"valor": "B", "texto": "Fazendo algo diferente e cheio de aventura."},
            {"valor": "C", "texto": "Ficando tranquilo em casa, curtindo meu tempo."},
            {"valor": "D", "texto": "Explorando lugares novos e conhecendo pessoas."},
        ],
        "frutas": {
            "A": ["morango", "banana"],
            "B": ["abacaxi", "manga"],
            "C": ["melancia", "maca"],
            "D": ["laranja", "uva"],
        },
    },
    {
        "id": 2,
        "texto": "Como seus amigos descreveriam você?",
        "alternativas": [
            {"valor": "A", "texto": "Divertido e carismático."},
            {"valor": "B", "texto": "Corajoso e cheio de atitude."},
            {"valor": "C", "texto": "Tranquilo e companheiro."},
            {"valor": "D", "texto": "Animado e otimista."},
        ],
        "frutas": {
            "A": ["morango", "banana"],
            "B": ["abacaxi", "manga"],
            "C": ["melancia", "maca"],
            "D": ["laranja", "uva"],
        },
    },
    {
        "id": 3,
        "texto": "Escolha a cor que mais combina com você.",
        "alternativas": [
            {"valor": "A", "texto": "Vermelho."},
            {"valor": "B", "texto": "Amarelo."},
            {"valor": "C", "texto": "Verde."},
            {"valor": "D", "texto": "Laranja."},
        ],
        "frutas": {
            "A": ["morango", "maca"],
            "B": ["abacaxi", "banana"],
            "C": ["melancia", "uva"],
            "D": ["laranja", "manga"],
        },
    },
    {
        "id": 4,
        "texto": "Quando aparece um problema inesperado, você...",
        "alternativas": [
            {"valor": "A", "texto": "Conversa com alguém e tenta resolver junto."},
            {"valor": "B", "texto": "Enfrenta a situação sem fugir do desafio."},
            {"valor": "C", "texto": "Pensa com calma e procura uma solução."},
            {"valor": "D", "texto": "Procura enxergar o lado positivo e tenta novamente."},
        ],
        "frutas": {
            "A": ["morango", "melancia"],
            "B": ["abacaxi", "manga"],
            "C": ["melancia", "maca"],
            "D": ["laranja", "banana"],
        },
    },
    {
        "id": 5,
        "texto": "Qual lugar você escolheria para relaxar?",
        "alternativas": [
            {"valor": "A", "texto": "Um parque cheio de amigos e diversão."},
            {"valor": "B", "texto": "Uma trilha ou um lugar para explorar."},
            {"valor": "C", "texto": "Uma praia tranquila, com sombra e brisa."},
            {"valor": "D", "texto": "Um lugar ensolarado, com música e atividades."},
        ],
        "frutas": {
            "A": ["morango", "banana"],
            "B": ["abacaxi", "manga"],
            "C": ["melancia", "uva"],
            "D": ["laranja", "maca"],
        },
    },
    {
        "id": 6,
        "texto": "Em um trabalho em grupo, qual é seu papel?",
        "alternativas": [
            {"valor": "A", "texto": "Animo o grupo e aproximo todo mundo."},
            {"valor": "B", "texto": "Tomo a iniciativa e encaro os desafios."},
            {"valor": "C", "texto": "Organizo as ideias e ajudo os colegas."},
            {"valor": "D", "texto": "Trago ideias criativas e entusiasmo."},
        ],
        "frutas": {
            "A": ["morango", "banana"],
            "B": ["abacaxi", "manga"],
            "C": ["melancia", "maca"],
            "D": ["laranja", "uva"],
        },
    },
    {
        "id": 7,
        "texto": "Qual qualidade você mais valoriza em si?",
        "alternativas": [
            {"valor": "A", "texto": "Simpatia."},
            {"valor": "B", "texto": "Coragem."},
            {"valor": "C", "texto": "Lealdade."},
            {"valor": "D", "texto": "Criatividade."},
        ],
        "frutas": {
            "A": ["morango", "laranja"],
            "B": ["abacaxi", "manga"],
            "C": ["melancia", "maca"],
            "D": ["uva", "banana"],
        },
    },
    {
        "id": 8,
        "texto": "Quando conhece alguém novo, você...",
        "alternativas": [
            {"valor": "A", "texto": "Puxa conversa e tenta fazer amizade."},
            {"valor": "B", "texto": "Age com confiança e mostra sua personalidade."},
            {"valor": "C", "texto": "Observa primeiro e vai se soltando aos poucos."},
            {"valor": "D", "texto": "Fica animado para descobrir coisas sobre a pessoa."},
        ],
        "frutas": {
            "A": ["morango", "banana"],
            "B": ["abacaxi", "laranja"],
            "C": ["melancia", "maca"],
            "D": ["uva", "manga"],
        },
    },
    {
        "id": 9,
        "texto": "Escolha uma atividade para fazer agora.",
        "alternativas": [
            {"valor": "A", "texto": "Jogar algo divertido com os amigos."},
            {"valor": "B", "texto": "Praticar esportes ou experimentar uma aventura."},
            {"valor": "C", "texto": "Desenhar, ouvir música ou descansar."},
            {"valor": "D", "texto": "Conhecer algo novo ou inventar alguma coisa."},
        ],
        "frutas": {
            "A": ["morango", "banana"],
            "B": ["abacaxi", "laranja"],
            "C": ["melancia", "uva"],
            "D": ["manga", "maca"],
        },
    },
    {
        "id": 10,
        "texto": "Se pudesse ter um superpoder, qual escolheria?",
        "alternativas": [
            {"valor": "A", "texto": "Fazer qualquer pessoa sorrir."},
            {"valor": "B", "texto": "Ter força e coragem extraordinárias."},
            {"valor": "C", "texto": "Proteger e ajudar quem você ama."},
            {"valor": "D", "texto": "Ter energia ilimitada para explorar o mundo."},
        ],
        "frutas": {
            "A": ["morango", "banana"],
            "B": ["abacaxi", "manga"],
            "C": ["melancia", "maca"],
            "D": ["laranja", "uva"],
        },
    },
]


# Create your views here.
def home_page(request):
    return render(request, 'home_page.html')


def about_page(request):
    return render(request, 'about.html')


def food_health_page(request):
    return render(request, 'food_and_health.html')


def well_being_page(request):
    return render(request, 'well_being.html')


def quiz_page(request):
    if request.method == "POST":

        # Recebe as 10 respostas
        respostas = {}

        for i in range(1, 11):
            respostas[f"q{i}"] = request.POST.get(f"q{i}")

        # Converte as respostas para números
        pontuacao = 0
        print(respostas)
        for resposta in respostas.values():
            if resposta is not None:
                pontuacao += int(resposta)

        # Define o resultado
        if pontuacao >= 25:
            resultado = (
                "Parabéns! Seus hábitos apresentam várias escolhas positivas. "
                "Continue cuidando da sua alimentação, hidratação, atividade física e descanso!"
            )

        elif pontuacao >= 17:
            resultado = (
                "Você está no caminho certo! Algumas pequenas mudanças podem "
                "melhorar ainda mais seus hábitos e contribuir para uma vida mais saudável."
            )

        elif pontuacao >= 9:
            resultado = (
                "Existem alguns hábitos que podem ser melhorados. "
                "Que tal começar com pequenas mudanças no dia a dia?"
            )

        else:
            resultado = (
                "Que tal começar aos poucos? Pequenas mudanças na alimentação, "
                "atividade física, hidratação e sono podem fazer uma grande diferença."
            )

        return render(request, "result.html", {
            "respostas": respostas,
            "pontuacao": pontuacao,
            "resultado": resultado,
        })

    return render(request, 'quiz.html')


def quiz_frutas(request):
    if request.method == "GET":
        return render(request, 'quizzes/quiz1.html')

    if request.method == "POST":
        resultado, maior_pontuacao = resultado_quiz1(request)
        return render(request, "result.html", {
            "resultado": resultado,
            "pontuacao": maior_pontuacao,
        })


def resultado_quiz1(request):
    pontuacoes = {fruta: 0 for fruta in FRUTAS}
    print(request.POST)
    # Valida as 10 respostas no servidor.
    for pergunta in PERGUNTAS:
        resposta = request.POST.get(f"q{pergunta['id']}")

        print(resposta)

    for fruta in pergunta["frutas"][resposta]:
        pontuacoes[fruta] += 1

    maior_pontuacao = max(pontuacoes.values())
    empatadas = [
        fruta
        for fruta, pontos in pontuacoes.items()
        if pontos == maior_pontuacao
    ]

    resultado = FRUTAS[random.choice(empatadas)]

    return resultado, maior_pontuacao



