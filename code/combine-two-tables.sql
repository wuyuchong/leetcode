select
  person.FirstName,
  person.LastName,
  address.City,
  address.State
from
  Person person
left join
  Address address
on
  person.PersonId = address.PersonId
