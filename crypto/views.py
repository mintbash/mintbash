# Imports
from django.views.generic import View
from django.shortcuts import render, redirect
from django.http import JsonResponse
import requests


# Views
class HomeView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, "crypto/home.html", context=context)


class ChartView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, "crypto/charts.html", context=context)


def get_pool_data(request):
    timespan = request.GET.get("timespan", None)
    response = requests.get(f"https://api.blockchain.info/pools?timespan={timespan}")
    data = response.json()
    print("i am data", data)
    return JsonResponse(data)


def chartss(request):
    chart_name = request.GET.get("chart", None)
    timespan = request.GET.get("timespan", None)
    response = requests.get(
        f"https://api.blockchain.info/charts/{chart_name}?timespan={timespan}"
    )
    data = response.json()
    return JsonResponse(data)


def get_block_account(request):
    response = requests.get("https://blockchain.info/q/getblockcount")
    data = response.text
    data = {"content": data}
    return JsonResponse(data)


def get_latest_hash(request):
    response = requests.get("https://blockchain.info/q/latesthash")
    data = response.text
    data = {"content": data}
    return JsonResponse(data)


def get_bc_per_block(request):
    response = requests.get("https://blockchain.info/q/bcperblock")
    data = response.text
    data = {"content": data}
    return JsonResponse(data)


def get_difficulty(request):
    response = requests.get("https://blockchain.info/q/getdifficulty")
    data = response.text
    data = {"content": data}
    return JsonResponse(data)


def get_total_bc(request):
    response = requests.get("https://blockchain.info/q/totalbc")
    data = response.text
    data = {"content": data}
    return JsonResponse(data)


def get_probablity(request):
    response = requests.get("https://blockchain.info/q/probability")
    data = response.text
    data = {"content": data}
    return JsonResponse(data)


def get_hash_to_win(request):
    response = requests.get("https://blockchain.info/q/hashestowin")
    data = response.text
    data = {"content": data}
    return JsonResponse(data)


def get_next_re_target(request):
    response = requests.get("https://blockchain.info/q/nextretarget")
    data = response.text
    data = {"content": data}
    return JsonResponse(data)


def get_unconfirmed_count(request):
    response = requests.get("https://blockchain.info/q/unconfirmedcount")
    data = response.text
    data = {"content": data}
    return JsonResponse(data)


def get_market_cap(request):
    response = requests.get("https://blockchain.info/q/marketcap")
    data = response.text
    data = {"content": data}
    return JsonResponse(data)


def get_stats(request):
    response = requests.get("https://api.blockchain.info/stats")
    data = response.text
    data = {"content": data}
    return JsonResponse(data)


def get_24_hour_btcsent(request):
    response = requests.get("https://blockchain.info/q/24hrbtcsent")
    data = response.text
    data = {"content": data}
    return JsonResponse(data)
