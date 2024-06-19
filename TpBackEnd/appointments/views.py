from django.shortcuts import render, get_object_or_404, redirect
from .models import Doctor, Appointment, Specialty
from .forms import AppointmentForm
from django.contrib.auth.decorators import login_required

def specialty_doctors(request, specialty_name):
    specialty = get_object_or_404(Specialty, name=specialty_name)
    doctors = Doctor.objects.filter(specialty=specialty)
    return render(request, 'appointments/specialty_doctors.html', {'specialty': specialty, 'doctors': doctors})

@login_required
def book_appointment(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.doctor = doctor
            appointment.patient = request.user
            appointment.save()
            return redirect('appointment_success')
    else:
        form = AppointmentForm()
    return render(request, 'appointments/book_appointment.html', {'form': form, 'doctor': doctor})

def appointment_success(request):
    return render(request, 'appointments/appointment_success.html')