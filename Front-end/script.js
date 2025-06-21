// // EduGrades JavaScript Functions

// // Utility Functions
// function showAlert(message, type = 'info') {
//     const alertDiv = document.createElement('div');
//     alertDiv.className = `alert alert-${type} alert-dismissible fade show`;
//     alertDiv.innerHTML = `
//         ${message}
//         <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
//     `;
//     document.body.insertBefore(alertDiv, document.body.firstChild);
    
//     // Auto dismiss after 5 seconds
//     setTimeout(() => {
//         if (alertDiv.parentNode) {
//             alertDiv.remove();
//         }
//     }, 5000);
// }

// // Form Validation
// function validateForm(formId) {
//     const form = document.getElementById(formId);
//     if (!form) return false;
    
//     const requiredFields = form.querySelectorAll('[required]');
//     let isValid = true;
    
//     requiredFields.forEach(field => {
//         if (!field.value.trim()) {
//             field.classList.add('is-invalid');
//             isValid = false;
//         } else {
//             field.classList.remove('is-invalid');
//             field.classList.add('is-valid');
//         }
//     });
    
//     return isValid;
// }

// // Login Form Handler
// document.addEventListener('DOMContentLoaded', function() {
//     // Student Login Form
//     const studentLoginForm = document.getElementById('studentLoginForm');
//     if (studentLoginForm) {
//         studentLoginForm.addEventListener('submit', function(e) {
//             e.preventDefault();
            
//             const studentName = document.getElementById('student_name').value.trim();
//             const studentCode = document.getElementById('student_code').value.trim();
            
            
//         });
//     }
    
//     // Admin Login Form
//     const adminLoginForm = document.getElementById('adminLoginForm');
//     if (adminLoginForm) {
//         adminLoginForm.addEventListener('submit', function(e) {
//             e.preventDefault();
            
//             const username = document.getElementById('admin_username').value.trim();
//             const password = document.getElementById('admin_password').value.trim();
            
//             if (username && password) {
//                 // Simulate login success - In real app, this would be handled by Django
//                 showAlert('Connexion administrateur réussie! Redirection...', 'success');
//                 setTimeout(() => {
//                     window.location.href = 'admin-dashboard.html';
//                 }, 1500);
//             } else {
//                 showAlert('Veuillez remplir tous les champs requis.', 'danger');
//             }
//         });
//     }
// });

// // Search and Filter Functions
// function setupSearch(searchInputId, tableBodyId) {
//     const searchInput = document.getElementById(searchInputId);
//     const tableBody = document.getElementById(tableBodyId);
    
//     if (searchInput && tableBody) {
//         searchInput.addEventListener('input', function() {
//             const searchTerm = this.value.toLowerCase();
//             const rows = tableBody.querySelectorAll('tr');
            
//             rows.forEach(row => {
//                 const text = row.textContent.toLowerCase();
//                 row.style.display = text.includes(searchTerm) ? '' : 'none';
//             });
//         });
//     }
// }

// // CRUD Operations for Students
// function editStudent(studentCode) {
//     // In a real application, this would fetch student data from Django backend
//     showAlert(`Modification de l'étudiant ${studentCode}`, 'info');
    
//     // Show edit modal with populated data
//     const editModal = new bootstrap.Modal(document.getElementById('editStudentModal'));
//     editModal.show();
    
//     // Populate form fields (example)
//     document.getElementById('edit_student_code').value = studentCode;
//     document.getElementById('edit_student_name').value = 'Nom de l\'étudiant';
// }

// function viewStudent(studentCode) {
//     showAlert(`Affichage des détails de l'étudiant ${studentCode}`, 'info');
//     // Redirect to student detail page or show modal
// }

// function deleteStudent(studentCode) {
//     if (confirm(`Êtes-vous sûr de vouloir supprimer l'étudiant ${studentCode} ?`)) {
//         showAlert(`Étudiant ${studentCode} supprimé avec succès`, 'success');
//         // In real app, make AJAX request to Django backend
//     }
// }

// // CRUD Operations for Subjects
// function editSubject(subjectCode) {
//     showAlert(`Modification de la matière ${subjectCode}`, 'info');
    
//     const editModal = new bootstrap.Modal(document.getElementById('editSubjectModal'));
//     editModal.show();
    
//     // Populate form fields
//     document.getElementById('edit_subject_code').value = subjectCode;
//     document.getElementById('edit_subject_name').value = 'Nom de la matière';
// }

// function viewSubject(subjectCode) {
//     showAlert(`Affichage des détails de la matière ${subjectCode}`, 'info');
// }

// function deleteSubject(subjectCode) {
//     if (confirm(`Êtes-vous sûr de vouloir supprimer la matière ${subjectCode} ?`)) {
//         showAlert(`Matière ${subjectCode} supprimée avec succès`, 'success');
//     }
// }

// // CRUD Operations for Grades
// function editGrade(gradeId) {
//     showAlert(`Modification de la note ID: ${gradeId}`, 'info');
//     // Show edit modal or redirect to edit page
// }

// function deleteGrade(gradeId) {
//     if (confirm('Êtes-vous sûr de vouloir supprimer cette note ?')) {
//         showAlert('Note supprimée avec succès', 'success');
//         // In real app, make AJAX request to Django backend
//     }
// }

// // Export Functions
// function exportGrades() {
//     showAlert('Export des notes en cours...', 'info');
//     // In real app, this would trigger a download from Django backend
//     setTimeout(() => {
//         showAlert('Export terminé! Le fichier a été téléchargé.', 'success');
//     }, 2000);
// }

// // Filter Reset
// function resetFilters() {
//     const filters = document.querySelectorAll('select[id^="filter"], input[id^="search"]');
//     filters.forEach(filter => {
//         filter.value = '';
//         if (filter.type === 'text') {
//             filter.dispatchEvent(new Event('input'));
//         }
//     });
//     showAlert('Filtres réinitialisés', 'info');
// }

// // Initialize Search Functions
// document.addEventListener('DOMContentLoaded', function() {
//     // Setup search for different pages
//     setupSearch('searchStudent', 'studentsTableBody');
//     setupSearch('searchSubject', 'subjectsTableBody');
//     setupSearch('searchGrade', 'gradesTableBody');
    
//     // Add fade-in animation to cards
//     const cards = document.querySelectorAll('.card');
//     cards.forEach((card, index) => {
//         setTimeout(() => {
//             card.classList.add('fade-in-up');
//         }, index * 100);
//     });
// });

// // File Upload Handler
// function handleFileUpload(inputId) {
//     const fileInput = document.getElementById(inputId);
//     if (fileInput) {
//         fileInput.addEventListener('change', function() {
//             const file = this.files[0];
//             if (file) {
//                 const fileSize = (file.size / 1024 / 1024).toFixed(2); // MB
//                 const fileName = file.name;
                
//                 if (fileSize > 5) {
//                     showAlert('Le fichier est trop volumineux (max 5MB)', 'danger');
//                     this.value = '';
//                     return;
//                 }
                
//                 if (!fileName.toLowerCase().endsWith('.csv')) {
//                     showAlert('Seuls les fichiers CSV sont acceptés', 'danger');
//                     this.value = '';
//                     return;
//                 }
                
//                 showAlert(`Fichier sélectionné: ${fileName} (${fileSize}MB)`, 'success');
//             }
//         });
//     }
// }

// // Initialize file upload handlers
// document.addEventListener('DOMContentLoaded', function() {
//     handleFileUpload('csv_file');
// });

// // Form Submission Handlers
// function setupFormHandlers() {
//     // Add Student Form
//     const addStudentForm = document.querySelector('#addStudentModal form');
//     if (addStudentForm) {
//         addStudentForm.addEventListener('submit', function(e) {
//             e.preventDefault();
//             if (validateForm('addStudentModal')) {
//                 showAlert('Étudiant ajouté avec succès!', 'success');
//                 bootstrap.Modal.getInstance(document.getElementById('addStudentModal')).hide();
//             }
//         });
//     }
    
//     // Add Subject Form
//     const addSubjectForm = document.querySelector('#addSubjectModal form');
//     if (addSubjectForm) {
//         addSubjectForm.addEventListener('submit', function(e) {
//             e.preventDefault();
//             if (validateForm('addSubjectModal')) {
//                 showAlert('Matière créée avec succès!', 'success');
//                 bootstrap.Modal.getInstance(document.getElementById('addSubjectModal')).hide();
//             }
//         });
//     }
    
//     // Add Grade Form
//     const addGradeForm = document.querySelector('#addGradeModal form');
//     if (addGradeForm) {
//         addGradeForm.addEventListener('submit', function(e) {
//             e.preventDefault();
//             if (validateForm('addGradeModal')) {
//                 showAlert('Note enregistrée avec succès!', 'success');
//                 bootstrap.Modal.getInstance(document.getElementById('addGradeModal')).hide();
//             }
//         });
//     }
    
//     // CSV Upload Form
//     const csvUploadForm = document.querySelector('#uploadCsvModal form');
//     if (csvUploadForm) {
//         csvUploadForm.addEventListener('submit', function(e) {
//             e.preventDefault();
//             const fileInput = document.getElementById('csv_file');
//             if (fileInput && fileInput.files[0]) {
//                 showAlert('Import en cours... Veuillez patienter.', 'info');
//                 // Simulate upload progress
//                 setTimeout(() => {
//                     showAlert('Import réussi! 45 notes ont été mises à jour.', 'success');
//                     bootstrap.Modal.getInstance(document.getElementById('uploadCsvModal')).hide();
//                 }, 3000);
//             } else {
//                 showAlert('Veuillez sélectionner un fichier CSV.', 'danger');
//             }
//         });
//     }
// }

// // Initialize form handlers when DOM is ready
// document.addEventListener('DOMContentLoaded', function() {
//     setupFormHandlers();
// });

// // Real-time Grade Validation
// function setupGradeValidation() {
//     const gradeInput = document.getElementById('grade_value');
//     if (gradeInput) {
//         gradeInput.addEventListener('input', function() {
//             const value = parseFloat(this.value);
//             if (value < 0 || value > 20) {
//                 this.classList.add('is-invalid');
//                 showAlert('La note doit être comprise entre 0 et 20', 'warning');
//             } else {
//                 this.classList.remove('is-invalid');
//                 this.classList.add('is-valid');
//             }
//         });
//     }
// }

// // Initialize grade validation
// document.addEventListener('DOMContentLoaded', function() {
//     setupGradeValidation();
// });

// // Theme Toggle (Optional Feature)
// function toggleTheme() {
//     const body = document.body;
//     body.classList.toggle('dark-theme');
//     localStorage.setItem('theme', body.classList.contains('dark-theme') ? 'dark' : 'light');
// }

// // Load saved theme
// document.addEventListener('DOMContentLoaded', function() {
//     const savedTheme = localStorage.getItem('theme');
//     if (savedTheme === 'dark') {
//         document.body.classList.add('dark-theme');
//     }
// });