const cur2Format = new Intl.NumberFormat("en-CA", {
    style: "currency",
    currency: "CAD",
    minimumFractionDigits: 2,
    maximumFractionDigits: 2,
  });
  
  let date = prompt("Enter Date (YYYY-MM-DD):");
  let memberName = prompt("Enter Member Name:");
  let street = prompt("Enter Street Address:");
  let city = prompt("Enter City:");
  let province = prompt("Enter Province:");
  let postal = prompt("Enter Postal Code:");
  let homePhone = prompt("Enter Home Phone:");
  let cellPhone = prompt("Enter Cell Phone:");
  let siteNumber = parseInt(prompt("Enter Site Number (1-100):"));
  let membershipType = prompt("Enter Membership Type (S for Standard, E for Executive):").toUpperCase();
  let alternateMembers = parseInt(prompt("Enter Number of Alternate Members:"));
  let weeklyCleaning = prompt("Weekly Site Cleaning? (Y/N):").toUpperCase() === "Y";
  let videoSurveillance = prompt("Video Surveillance? (Y/N):").toUpperCase() === "Y";
  
  let data = {
    date,
    memberName,
    street,
    city,
    province,
    postal,
    homePhone,
    cellPhone,
    siteNumber,
    membershipType,
    alternateMembers,
    weeklyCleaning,
    videoSurveillance
  };
  
  const charges = calculateCharges(data);
  displayReceipt(data, charges);
  
  function calculateCharges(input) {
    const evenSiteCharge = 80.0;
    const oddSiteCharge = 120.0;
    const altCharge = 5.0;
    const cleaningCharge = 50.0;
    const surveillanceCharge = 35.0;
    const duesStandard = 75.0;
    const duesExecutive = 150.0;
    const HSTRate = 0.15;
    const processingFee = 59.99;
    const cancelRate = 0.6;
  
    let siteCharge;
    if (input.siteNumber % 2 === 0) {
      siteCharge = evenSiteCharge;
    } else {
      siteCharge = oddSiteCharge;
    }
    let extraCharges = input.alternateMembers * altCharge;

    if (input.weeklyCleaning) {
      extraCharges += cleaningCharge;
    } else {
      extraCharges += 0;
    }
    
    if (input.videoSurveillance) {
      extraCharges += surveillanceCharge;
    } else {
      extraCharges += 0;
    }
    const subtotal = siteCharge + extraCharges;
    const tax = subtotal * HSTRate;
    //const membershipDues = input.membershipType === "S" ? duesStandard : duesExecutive;
    // This line above is another style for if else statements. 
    // I looked further into this to see what oither possibilities are out there.

    let membershipDues;
if (input.membershipType === "S") {
    membershipDues = duesStandard;
} else {
    membershipDues = duesExecutive;
}

    const totalMonthlyBeforeDues = subtotal + tax;
    const totalMonthlyFees = totalMonthlyBeforeDues + membershipDues;
    const yearlyFees = totalMonthlyFees * 12;
    const monthlyPayment = (yearlyFees + processingFee) / 12;
    const cancellationFee = yearlyFees * cancelRate;
  
    return {
      siteCharge,
      extraCharges,
      subtotal,
      tax,
      membershipDues,
      totalMonthlyBeforeDues,
      totalMonthlyFees,
      yearlyFees,
      monthlyPayment,
      cancellationFee,
    };
  }
  
  function displayReceipt(input, charges) {
    let membershipLabel;
    if (input.membershipType === 'S') {
      membershipLabel = 'Standard';
    } else {
      membershipLabel = 'Executive';
    }
  
    document.writeln('<table class="receipttable">');
    document.writeln('<tr><td colspan="2" class="mainhead">St. John’s Marina & Yacht Club<br>Yearly Member Receipt</td></tr>');
  
    document.writeln('<tr><td colspan="2" class="section-title">Client Name and Address:</td></tr>');
    document.writeln('<tr><td colspan="2">' +
      input.memberName + '<br>' +
      input.street + '<br>' +
      input.city + ', ' + input.province + ' ' + input.postal + '<br>' +
      'Phone: ' + input.homePhone + ' (H)<br>' +
      input.cellPhone + ' (C)' +
      '</td></tr>');
  
    document.writeln('<tr><td class="label">Site #:</td><td class="amount">' + input.siteNumber + '</td></tr>');
    document.writeln('<tr><td class="label">Member type:</td><td class="amount">' + membershipLabel + '</td></tr>');
  
    document.writeln('<tr><td class="label">Alternate members:</td><td class="amount">' + input.alternateMembers + '</td></tr>');
    document.writeln('<tr><td class="label">Weekly site cleaning:</td><td class="amount">' + (input.weeklyCleaning ? "Yes" : "No") + '</td></tr>');
    document.writeln('<tr><td class="label">Video surveillance:</td><td class="amount">' + (input.videoSurveillance ? "Yes" : "No") + '</td></tr>');
  
    document.writeln('<tr><td class="label">Site charges:</td><td class="amount">' + cur2Format.format(charges.siteCharge) + '</td></tr>');
    document.writeln('<tr><td class="label">Extra charges:</td><td class="amount">' + cur2Format.format(charges.extraCharges) + '</td></tr>');
  
    document.writeln('<tr><td class="label">Subtotal:</td><td class="amount">' + cur2Format.format(charges.subtotal) + '</td></tr>');
    document.writeln('<tr><td class="label">Sales tax (HST):</td><td class="amount">' + cur2Format.format(charges.tax) + '</td></tr>');
  
    document.writeln('<tr><td class="label">Total monthly charges:</td><td class="amount">' + cur2Format.format(charges.totalMonthlyBeforeDues) + '</td></tr>');
    document.writeln('<tr><td class="label">Monthly dues:</td><td class="amount">' + cur2Format.format(charges.membershipDues) + '</td></tr>');
  
    document.writeln('<tr><td class="label">Total monthly fees:</td><td class="amount">' + cur2Format.format(charges.totalMonthlyFees) + '</td></tr>');
    document.writeln('<tr><td class="label">Total yearly fees:</td><td class="amount">' + cur2Format.format(charges.yearlyFees) + '</td></tr>');
  
    document.writeln('<tr><td class="label">Monthly payment:</td><td class="amount">' + cur2Format.format(charges.monthlyPayment) + '</td></tr>');
  
    document.writeln('<tr><td class="label">Issued:</td><td class="amount">' + input.date + '</td></tr>');
    document.writeln('<tr><td class="label">HST Reg No:</td><td class="amount">549-33-5849-47</td></tr>');
    document.writeln('<tr><td class="label">Cancellation fee:</td><td class="amount">' + cur2Format.format(charges.cancellationFee) + '</td></tr>');
  
    document.writeln('</table>');
  }