from flask import Flask, render_template, request

def storage(name):
    out = open ('data.txt', 'a')
    out.write (name + "\n")
    out.close ( )

def countVote(value):
    candidate = " "
    if value == "1":
        candidate = "1"
    elif value == "2":
        candidate = "2"
    elif value == "3":
        candidate = "3"
    elif value == "4":
        candidate = "4"
    elif value == "5":
        candidate = "5"
    elif value == "6":
        candidate = "6"
    else:
        pass
    return candidate
def results():

    allCandidates = {}
    candidate1 = 0
    candidate2 = 0
    candidate3 = 0
    candidate4 = 0
    candidate5 = 0
    candidate6 = 0
    f = open('data.txt', 'r')

    for line in f:
        vote = line.rstrip("\n")
        if vote == "1":
            candidate1 += 1
        elif vote == "2":
            candidate2 += 1
        elif vote == "3":
            candidate3 += 1
        elif vote == "4":
            candidate4 += 1
        elif vote == "5":
            candidate5 += 1
        elif vote == "6":
            candidate6 += 1
        else:
            break
    f.close ( )
    allCandidates[0] = candidate1
    allCandidates[1] = candidate2
    allCandidates[2] = candidate3
    allCandidates[3] = candidate4
    allCandidates[4] = candidate5
    allCandidates[5] = candidate6






