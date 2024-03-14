# Track Corporate Assets
  This is a Django app to track corporate assets such as phones, tablets, laptops and other gears handed out to employees. The application might be used by several companies. 
  Each company might add all or some of its employees. Each company and its staff might delegate one or more devices to employees for a certain period of time.
  Each company should be able to see when a Device was checked out and returned. Each device should have a log of what condition it was handed out and returned.

## Base URL
  The base URL for all API endpoints is: https://track-corporate-assets.onrender.com/

## Endpoints

### Companies

  - **GET** `/companies/`
    - Description: Retrieve a list of all companies.
  - **GET** `/companies/{companie_id}`
    - Description: Retrieve details of a specific company.
  - **GET** `/companies/?name={companie_name}`
    - Description: Retrieve details of a relevant company.
  - **POST** `/companies/`
    - Description: Create a new company.
  - **PUT** `/companies/{companie_id}`
    - Description: Update information of a specific company.
  - **DELETE** `/companies/{companie_id}`
    - Description: Delete a specific company.

### Employees

  - **GET** `/employees/`
    - Description: Retrieve a list of all employees.
  - **GET** `/employees/{employee_id}`
    - Description: Retrieve details of a specific employee.
  - **GET** `/employees/?name={employee_name}`
    - Description: Retrieve details of a relevant employee.
  - **POST** `/employees/`
    - Description: Create a new employee.
  - **PUT** `/employees/{employee_id}`
    - Description: Update information of a specific employee.
  - **DELETE** `/employees/{employee_id}`
    - Description: Delete a specific employee.
 
### Devices
  - **GET** `/devices/`
    - Description: Retrieve a list of all devices.
  - **GET** `/devices/{device_id}`
    - Description: Retrieve details of a specific device.
  - **GET** `/devices/?name={device_name}`
    - Description: Retrieve details of a relevant device.
  - **POST** `/devices/`
    - Description: Create a new device.
  - **PUT** `/devices/{device_id}`
    - Description: Update information of a specific device.
  - **DELETE** `/devices/{device_id}`
    - Description: Delete a specific device.

### Devices Assign
  - **GET** `/assign/`
    - Description: Retrieve a list of all devices Assign details.
  - **GET** `/assign/{assign_id}`
    - Description: Retrieve details of a specific device assignment.
  - **POST** `/assign/`
    - Description: Create a new device assignment.
  - **PUT** `/assign/{assign_id}`
    - Description: Update information of a specific device assignment.
  - **DELETE** `/assign/{assign_id}`
    - Description: Delete a specific device assignment.
      
### Devices Returned
   - **GET** `/returned/`
    - Description: Retrieve a list of all devices Returned update.
  - **GET** `/returned/{returned_id}`
    - Description: Retrieve details of a specific device  Returned update.
  - **POST** `/returned/`
    - Description: Create a new device  Returned update.
  - **PUT** `/returned/{returned_id}`
    - Description: Update information of a specific device  Returned update.
  - **DELETE** `/returned/{returned_id}`
    - Description: Delete a specific device  Returned update.

## Support
  For any questions or issues, please contact (
     📩  hmnizum1714032@gmail.com
     📱 +8801981251861, +8801986119395
  )
  
## Database Entity Relationship Diagram
  [Download Diagram](https://drive.google.com/file/d/1hAUFU0HbzQjtmnGaWO6N2Alcm9DY3At0/view?usp=sharing)

![Untitled Diagram drawio (5)](https://github.com/H-M-Nizum/trackCorporateAssets/assets/106550437/c15065ee-32f3-4ece-ad73-2f45d5477244)
