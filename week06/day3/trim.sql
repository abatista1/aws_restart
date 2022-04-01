select trim(Name) 'Trimmed Name',
length(Name) 'Before Trim',
length(trim(Name)) 'After Trim'
from university.students;