from django.http import HttpResponseBadRequest
from django.shortcuts import render

from Task_1.services import password_generator


def task_1(request):
    """
    Request example:
    http://127.0.0.1:8000/FBV/alternative/?total_count=3&length=5&use_numbers=true&use_special_chars=true
    """

    total_count = request.GET.get("total_count")
    length = request.GET.get("length")
    use_numbers = request.GET.get("use_numbers")
    use_special_chars = request.GET.get("use_special_chars")

    if (
            not total_count
            or not length
            or not use_numbers
            or not use_special_chars
            or total_count.isdigit() is False
            or length.isdigit() is False
            or int(total_count) <= 0
            or int(length) <= 0
            or use_numbers not in ["true", "false"]
            or use_special_chars not in ["true", "false"]
    ):
        return render(request, "task_1.html", {"error": "Incorrect data in URL"})

    total_count = int(total_count)
    length = int(length)
    use_numbers = True if use_numbers == "true" else False
    use_special_chars = True if use_special_chars == "true" else False

    passwords_list = password_generator(total_count, length, use_numbers,
                                        use_special_chars)

    return render(request, "task_1.html",
                  {"passwords_list": passwords_list})
