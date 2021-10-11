import graph_tool.all as gt  # Biblioteca para GRAFO
from xml.dom import minidom


def verificarCaminho(raiz, alvo):
    h = [""]

    # raiz = 'q7'       #parametro
    # alvo = 'q16'      #parametro

    # print(f'r:{raiz}/a:{alvo}')

    g = gt.Graph()
    g.set_directed(True)  # criação do objeto
    v_name = g.new_vertex_property("string")  # referenciação da lista v_name com uma nova propriedade (label) criada para o vértice - tipo string
    e_action = g.new_edge_property(
        "string")  # referenciação da lista e_ord com uma nova propriedade criada para a descrilção da ação relacionada a aresta - tipo string

    # Criação dos vértices no grafo à partir do arquivo .jff do jFlap
    xmldoc = minidom.parse("tab.jff")  # Carregando arquivo do JFLAP
    itemlist = xmldoc.getElementsByTagName('state')  # Tag <state>
    n_Vertex = len(itemlist)
    for s in itemlist:
        v = g.add_vertex()
        v_name[v] = s.attributes['name'].value

    # Criação das arestas no grafo à partir do arquivo .jff do jFlap
    e_from = []
    itemlist = xmldoc.getElementsByTagName('from')  # Tag <from>
    n_Transition = len(itemlist)
    for s in itemlist:
        e_from.append(s.childNodes[0].nodeValue)
    e_to = []
    itemlist = xmldoc.getElementsByTagName('to')  # Tag <to>
    for s in itemlist:
        e_to.append(s.childNodes[0].nodeValue)
    e_read = []
    itemlist = xmldoc.getElementsByTagName('read')  # Tag <read>
    for s in itemlist:
        e_read.append(s.childNodes[0].nodeValue)

    for edge in range(n_Transition):
        e = g.add_edge(int(e_from[edge]), int(e_to[edge]))
        # e_action[e] = actions[int(e_read[edge])]
        e_action[e] = str(e_read[edge])
    # Lista de arestas criadas

    g_bfs = gt.Graph()  # criação do objeto para busca em Largura
    v_name_bfs = g_bfs.new_vertex_property("string")  # referenciação da lista v_name com uma nova propriedade (label) criada para o vértice - tipo string
    e_ord = g_bfs.new_edge_property("int")  # referenciação da lista e_ord com uma nova propriedade criada para a ordem de expansão - tipo int
    e_action_bfs = g_bfs.new_edge_property(
        "string")  # referenciação da lista e_ord com uma nova propriedade criada para a descrilção da ação relacionada a aresta - tipo string

    xmldoc = minidom.parse("tab.jff")  # Carregando arquivo do JFLAP
    itemlist = xmldoc.getElementsByTagName('state')  # Tag <state>
    n_Vertex = len(itemlist)
    for s in itemlist:
        v = g_bfs.add_vertex()
        v_name_bfs[v] = s.attributes['name'].value
    # Lista de vértices criados
    # print(list(v_name))

    # Busca em Largura (bfs) e geração das arestas
    index_raiz = list(v_name).index(raiz)
    ord = 1
    for edge in gt.bfs_iterator(g, g.vertex(index_raiz)):
        # print(v_name[int(edge.source())], "->", v_name[int(edge.target())])
        e = g_bfs.add_edge(int(edge.source()), int(edge.target()))
        e_ord[e] = ord
        e_action_bfs[e] = '(' + str(ord) + ') '  # + e_action[g.edge(int(edge.source()), int(edge.target()))]
        ord += 1

    class VisitorExample(gt.BFSVisitor):  # É um objeto visitante que é chamado nos pontos de evento dentro do algoritmo bfs_search()
        def __init__(self, name, time, name_time, v_color, dist, pred, e_color, e_action, e_ord):
            self.name = name
            self.time = time
            self.name_time = name_time
            self.fill_color = v_color
            self.dist = dist
            self.pred = pred
            self.color = e_color
            self.e_action = e_action
            self.e_ord = e_ord
            self.e_count = 0
            self.last_time = 0

        def discover_vertex(self, u):  # Invocado quando um vértice é encontrado pela primeira vez.
            self.name[u] = v_name[u]
            self.time[u] = self.last_time
            self.last_time += 1
            self.name_time[u] = str(self.name[u]) + "(" + str(self.time[u]) + ")"
            self.fill_color[u] = "white"

        def tree_edge(self, e):  # Invocado em cada aresta à medida que se torna um
            self.pred[e.target()] = int(e.source())  # membro das arestas que formam a árvore de pesquisa.
            self.dist[e.target()] = self.dist[e.source()] + 1
            e = g_bfs.add_edge(int(e.source()), int(e.target()))
            self.color[e] = "gray"
            self.e_action[e] = e_action[g.edge(int(e.source()), int(e.target()))]
            self.e_count += 1
            self.e_ord[e] = self.e_count

    # Busca em Largura (bfs) e geração das arestas
    # g_bfs = gt.Graph()                                      # criação do objeto para busca em Largura
    bfsv_name = g_bfs.new_vertex_property("string")  # referenciação da lista v_name_bfs com uma nova propriedade do vértice para o nome - tipo string
    bfsv_time = g_bfs.new_vertex_property("int")  # referenciação da lista v_time com uma nova propriedade do vértice para a ordem de expansão - tipo int
    bfsv_name_time = g_bfs.new_vertex_property(
        "string")  # referenciação da lista v_name_time com uma nova propriedade do vértice para o nome e ordem de expansão - tipo string
    bfsv_color = g_bfs.new_vertex_property("string")  # referenciação da lista v_color com uma nova propriedade do vértice para a cor - tipo string
    bfsv_dist = g_bfs.new_vertex_property("int")  # referenciação da lista v_dist como uma propriedade do vértice criada para a distância da raiz
    bfsv_pred = g_bfs.new_vertex_property("int64_t")  # referenciação da lista v_pred como uma propriedade do vértice para referenciar o predecessor (pai)
    bfse_color = g_bfs.new_edge_property("string")  # referenciação da lista e_color com uma nova propriedade da aresta para a cor - tipo string
    bfse_action = g_bfs.new_edge_property("string")  # referenciação da lista e_action_bfs com uma nova propriedade da aresta para a ação - tipo string
    bfse_ord = g_bfs.new_edge_property("string")  # referenciação da lista e_action_bfs com uma nova propriedade da aresta para a ação - tipo string

    index_raiz = list(v_name).index(raiz)

    gt.bfs_search(g, g.vertex(index_raiz),
                  VisitorExample(bfsv_name, bfsv_time, bfsv_name_time, bfsv_color, bfsv_dist, bfsv_pred, bfse_color, bfse_action, bfse_ord))

    index_alvo = list(bfsv_name).index(alvo)  # Localizando o índice do Estado a ser encontrado
    bfsv_color[index_raiz] = "#729fcf"
    bfsv_color[index_alvo] = "green"
    path = []  # array do caminho
    path.insert(0, bfsv_name[index_alvo])  # inserções sendo realizadas no início

    while index_alvo != index_raiz:
        e = g_bfs.edge(bfsv_pred[index_alvo], index_alvo)
        bfse_color[e] = "red"
        index_alvo = bfsv_pred[index_alvo]
        path.insert(0, bfsv_name[index_alvo])
        bfsv_color[index_alvo] = "#729fcf"

    # bfsv_color[index_raiz] = "#729fcf"; print("Cores Vértices.........:", list(bfsv_color))

    # print("Caminho encontrado.....:",path)                   # mostrando o caminho encontrado da raiz ao alvo
    return path
