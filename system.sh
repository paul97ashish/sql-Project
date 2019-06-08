#!/bin/bash

source venv/bin/activate

print_options () {
    echo "Press ENTER to continue..."
    read "" enter
    clear

    echo "Choose one of the following options (e.g. enter '3' for the third option)"
    echo "NOTE: you don't need to press enter once you entered you're command"
    echo ""
    echo "    1. View party information staying in room X and starting time T"
    echo "    2. View employee data"
    echo "    3. Add a new employee"
    echo "    4. Add a new hotel"
    echo "    5. View all rooms based on status"
    echo "    Enter 'q' to quit the system"
}

print_options
while read -n1 -rep "" && [[ $REPLY != q ]]; do
  
  case $REPLY in
    1) echo "Your choice was 1"
    read -p "Enter a starting Date (e.g. 2017-02-10): " date
    read -p "Enter a Space ID (e.g. 100): " space_id
    python -W ignore option1.py $date $space_id
    print_options;;
    
    2) echo "Your choice was 2"
    read -p "Enter a Name (e.g. Avye Mcdowell): " name

    python -W ignore option2.py $name
    print_options;;
    
    3) echo "Your choice was 3"
    read -p "Enter a unique ID (e.g. 2222222): " id
    read -p "Enter a Salary (e.g. 1992): " salary
    read -p "Enter a Starting date (e.g. 2017-02-10): " start_date
    read -p "Enter the First Name (e.g. Tristan): " name_first
    read -p "Enter the Last Name (e.g. Toupin): " name_last
    read -p "Enter the type of employee (e.g. Clerk): " type_
    read -p "Enter a Location (e.g. Valleyfield): " location

    python -W ignore option3.py $id $salary $start_date $name_first $name_last $type_ $location
    print_options;;
    
    4) echo "Your choice was 4"
    read -p "Enter a Location (e.g. Wonderland): " location
    read -p "Enter the area of the hotel (e.g. 1000): " total_area

    python -W ignore option4.py $location $total_area
    print_options;;
    
    5) echo "Your choice was 5"
    read -p "Enter a status (e.g. Available or Booked): " status

    python -W ignore option5.py $status
    print_options;;
  
  esac
done


echo ""

# kill falsk server
PROCESS=$(ps -fA | pgrep -f flask)
for p in $PROCESS
do
    kill $p || echo "An error occured!"
done

echo "Exited successfully"
