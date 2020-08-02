from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render
from board.models import Board
from django.shortcuts import redirect
from datetime import datetime
import requests
import js2py
msg = '제목, 작성자, 내용을 입력해주세요.'

def home(request):
    return render(request, "home.html")


def board(request):
    rsBoard = Board.objects.all()
    return render(request, "board_list.html", {
        'rsBoard': rsBoard})


# 유저가 처음으로 보는 페이지이고 from, import를 작성해야 함수 추가가능 -> urls.py로 이동

def board_write(request):
    return render(request, "board_write.html", )


def board_insert(request):
    btitle = request.POST["b_title"]
    bnote = request.POST['b_note']
    bwriter = request.POST['b_writer']
    bdate = datetime.now()

    if btitle != "" and bnote != "" and bwriter != "":
        rows = Board.objects.create(b_title=btitle, b_note=bnote, b_writer=bwriter, b_date=bdate)
        return redirect('/board')

    elif btitle == "" or bnote == "" or bwriter == "":

        return render(request, "board_write.html", {'message': msg})


def board_view(request):
    bno = request.GET['b_no']
    rsDetail = Board.objects.filter(b_no=bno)

    return render(request, "board_view.html", {
        'rsDetail': rsDetail})


def board_delete(request):
    bno = request.GET['b_no']
    rows = Board.objects.get(b_no=bno).delete()

    return redirect('/board')


def board_edit(request):
    bno = request.GET['b_no']
    rsDetail = Board.objects.filter(b_no=bno)

    return render(request, "board_edit.html", {'rsDetail': rsDetail})


def board_update(request):
    bno = request.POST['b_no']
    btitle = request.POST['b_title']
    bnote = request.POST['b_note']
    bwriter = request.POST['b_writer']
    bdate = datetime.now()

    if btitle != "" and bnote != "" and bwriter != "":
        rsDetail = Board.objects.filter(b_no=bno).update(b_title=btitle, b_note=bnote, b_writer=bwriter, b_date=bdate)
        return redirect('/board')

    elif btitle == "" or bnote == "" or bwriter == "":

        return render(request, "board_edit.html", {'message': msg, 'bno' : bno})




'''
    try:
        board = Board.objects.get(b_no=bno)
        if btitle != "":
            board.b_title = btitle
        if bnote != "":
            board.b_note = bnote
        if bwriter != "":
            board.b_writer = bwriter
        return render(request, "board_edit.html", {'message': msg})
        try:
            board.save()
            return redirect('/board')
        except ValueError:
            return requests.Response({"success": False, "msg": "에러입니다."})

    except ObjectDoesNotExist:
        return requests.Response({"success": False, "msg": "게시글 없음."})
'''