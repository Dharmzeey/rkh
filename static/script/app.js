var current_fs, next_fs, previous_fs; 


$(".next").click(function(){
	
	current_fs = $(this).parent();
	next_fs = $(this).parent().next();
	radioButtons = current_fs.find('input[type="radio"]');
	let selected = false;

  Array.from(radioButtons).forEach((radioButton) => {
    if (radioButton.checked) {
      selected = true;
			next_fs.show(); 
			current_fs.hide();
    }
  });

  if (!selected) {
		alert('Please select a candidate');
  }
	
	
});

$(".previous").click(function(){
	
	current_fs = $(this).parent();
	previous_fs = $(this).parent().prev();
	
	previous_fs.show(); 
	current_fs.hide();
});

