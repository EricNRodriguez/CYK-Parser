from production_rule import ProductionRule
from cyk_parser import CYKParser
from grammar import Grammar
from copy import deepcopy

def instantiate_grammar():
    # Nw = ProductionRule("Nw", ["w"])
    # Nh = ProductionRule("Nh", ["h"])
    # Ni = ProductionRule("Ni", ["i"])
    # Nl = ProductionRule("Nl", ["l"])
    # Ne = ProductionRule("Ne", ["e"])
    # Ns = ProductionRule("Ns", ["s"])
    # Nt = ProductionRule("Nt", ["t"])
    # Nd = ProductionRule("Nd", ["d"])
    # N0 = ProductionRule("N0", ["0"])
    # No = ProductionRule("No", ["o"])
    # Nsc = ProductionRule("Nsc", [";"])
    # Nrb = ProductionRule("Nrb", [")"])
    # Nlb = ProductionRule("Nlb", ["("])
    # Neq = ProductionRule("Neq", ["="])
    #
    # # while
    # W3 = ProductionRule("W3", [Nl, Ne])
    # W2 = ProductionRule("W2", [Ni, W3])
    # W1 = ProductionRule("W1", [Nh, W2])
    # W = ProductionRule("W", [Nw, W1])
    #
    # # do
    # K = ProductionRule("K", [Nd, No])
    #
    # # else
    # J2 = ProductionRule("J2", [Ns, Ne])
    # J1 = ProductionRule("J1", [Nl, J2])
    # J = ProductionRule("J", [Ne, J1])
    #
    # # let
    # P1 = ProductionRule("P1", [Ne, Nt])
    # P = ProductionRule("P", [Nl, P1])
    #
    # # epsilon
    # epsilon = ProductionRule("epsilon")
    #
    # # create rules
    # S0 = ProductionRule("S0")
    # S = ProductionRule("S")
    # L = ProductionRule("L")
    # E = ProductionRule("E")
    # E1 = ProductionRule("E1")
    # E2 = ProductionRule("E2")
    # E3 = ProductionRule("E3")
    # A = ProductionRule("A")
    # A1 = ProductionRule("A1")
    # A2 = ProductionRule("A2")
    # C = ProductionRule("C")
    # C1 = ProductionRule("C1")
    # C2 = ProductionRule("C2")
    # C3 = ProductionRule("C3")
    # H = ProductionRule("H")
    # V = ProductionRule("V")
    # B = ProductionRule("B")
    # N = ProductionRule("N")
    # D = ProductionRule("D")
    #
    #
    #
    # # add bodies
    # S0.add_bodys([S, L], [A, Nsc], [E, Nsc], [C, Nsc], [epsilon])
    # S.add_bodys([S, L], [A, Nsc], [E, Nsc], [C, Nsc])
    # L.add_bodys([A, Nsc], [E, Nsc], [C, Nsc])
    # E.add_bodys([Nlb, E1], [N, D], [N, N0], ["1"], ["2"], ["3"], ["4"], ["5"], ["6"], ["7"], ["8"], ["9"], ["x"], ["y"],
    #             ["z"])
    # E1.add_bodys([E, E2])
    # E2.add_bodys([B, E3])
    # E3.add_bodys(E, Nrb)
    # A.add_bodys([P, A1])
    # A1.add_bodys([V, A2])
    # A2.add_bodys([Neq, E])
    # C.add_bodys([C1, C3], [C1, H], [C1, S], [W, C2])
    # C1.add_bodys([W, C2])
    # C2.add_bodys([E, K])
    # C3.add_bodys([S, H])
    # H.add_bodys([K, S], [K])
    # B.add_bodys(["+"], ["-"], ["*"], [">"])
    # V.add_bodys(["x"], ["y"], ["z"])
    # N.add_bodys([N, D], [N, N0], ["1"], ["2"], ["3"], ["4"], ["5"], ["6"], ["7"], ["8"], ["9"])
    # D.add_bodys(["1"], ["2"], ["3"], ["4"], ["5"], ["6"], ["7"], ["8"], ["9"])
    #
    # return Grammar(
    #     [Nw, Nh, Ni, Nl, Ne, Ns, Nt, Nd, N0, No, Nsc, Nrb, Nlb, Neq, W3, W2, W1, W, K, J2, J1, J, P1, P, epsilon, S0, S,
    #      L, E, E1, E2, E3, A, A1, A2, C, C1, C2, C3, H, V, B, N, D],
    #     list("xyzwhilesdto1234567890o_+-*>;=()"),
    # S0)

    S = ProductionRule("S")
    VP = ProductionRule("VP")
    PP = ProductionRule("PP")
    NP = ProductionRule("NP")
    V = ProductionRule("V")
    P = ProductionRule("P")
    N = ProductionRule("N")
    Det = ProductionRule("Det")
    #
    S.add_bodys([NP, VP])
    VP.add_bodys([VP, PP], [V, NP], ["e"])
    PP.add_bodys([P,NP])
    NP.add_bodys([Det,N],["s"])
    V.add_bodys(["e"])
    P.add_bodys(["w"])
    N.add_bodys(["F"], ["f"])
    Det.add_bodys(["a"])

    return Grammar(
        [S,VP,PP,NP,V,P,N,Det],
        list("eswFfa"),
        S
    )


    # S = ProductionRule("S")
    # A = ProductionRule("A")
    # B = ProductionRule("B")
    # C = ProductionRule("C")
    # S.add_bodys([A,B], [B,C])
    # A.add_bodys([B,A],["a"])
    # B.add_bodys([C,C], ["b"])
    # C.add_bodys([A,B],["a"])
    #
    # return Grammar([S,A,B,C],list("ab"), S)
    #


def parse_string(fp):
    return "seaFwaf"


def main():
    cyk_parser = CYKParser(instantiate_grammar())

    string = parse_string("./test_file_path.txt")

    cyk_parser.parse(string)

    return

if __name__ == '__main__':
    main()

