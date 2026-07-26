// Validación de front-end reutilizable para formularios con clase "js-validate"
document.addEventListener('DOMContentLoaded', function () {
    const forms = document.querySelectorAll('form.js-validate');

    forms.forEach(function (form) {
        form.addEventListener('submit', function (event) {
            let valid = true;

            form.querySelectorAll('[required]').forEach(function (field) {
                clearError(field);
                if (!field.value || field.value.trim() === '') {
                    showError(field, 'Este campo es obligatorio.');
                    valid = false;
                }
            });

            // Validación específica: la fecha de un turno no puede ser pasada
            const dateField = form.querySelector('input[type="date"][name="date"]');
            if (dateField && dateField.value) {
                const today = new Date().toISOString().split('T')[0];
                if (dateField.value < today) {
                    showError(dateField, 'La fecha no puede ser anterior a hoy.');
                    valid = false;
                }
            }

            if (!valid) {
                event.preventDefault();
            }
        });
    });

    function showError(field, message) {
        let error = field.parentElement.querySelector('.js-error');
        if (!error) {
            error = document.createElement('span');
            error.className = 'js-error form-error';
            field.parentElement.appendChild(error);
        }
        error.textContent = message;
    }

    function clearError(field) {
        const error = field.parentElement.querySelector('.js-error');
        if (error) error.remove();
    }
});