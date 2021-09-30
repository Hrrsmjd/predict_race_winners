let Tbody = document.querySelector("tbody");
let TheadCell = document.querySelectorAll("thead th");
let AddRowButton = document.querySelector(".add-row-options button");
let DeleteIconWrapper = document.querySelectorAll(".icon-wrapper");

const HandleDelete = (e) => {
  let Row = e.target.parentNode.parentNode;
  let AllRows = Tbody.querySelectorAll("tr");

  if (AllRows.length > 1) {
    Row.remove();
  }
};

DeleteIconWrapper.forEach((EachIcon) => {
  EachIcon.addEventListener("click", HandleDelete);
});

const TableCellWorking = (TheadCell) => {
  TheadCell.forEach((element) => {
    element.addEventListener("click", (e) => {
      let id = e.target.id;

      document.querySelectorAll(`.${id} input`).forEach((EachElement) => {
        if (EachElement.classList.contains("active")) {
          EachElement.classList.remove("active");
          EachElement.removeAttribute("disabled");
        } else {
          EachElement.classList.add("active");
          EachElement.setAttribute("disabled", true);
        }
      });
    });
  });
};

TableCellWorking(TheadCell);

AddRowButton.addEventListener("click", (e) => {
  e.preventDefault();
  let HTML = `
     <tr>
            <td class="race">
                <input type="text" />
              </td>
              <td class="Horse">
                <input type="text" />
              </td>
              <td class="Weight">
                <input type="text" />
              </td>
              <td class="Age">
                <input type="text" />
              </td>
              <td class="Days">
                <input type="text" />
              </td>
              <td class="p_races">
                <input type="text" />
                   <div class="icon-wrapper">
                  <i class="far fa-trash-alt"></i>
                </div>
              </td>
            </tr>
            
            `;
  Tbody.insertAdjacentHTML("beforeend", HTML);

  let TdCellBody = document.querySelectorAll("tbody tr input");
  TdCellBody.forEach((Each) => {
    if (Each.classList.contains("active")) {
      let Class = Each.parentElement.classList[0];
      document.querySelectorAll(`.${Class} input`).forEach((EachInput) => {
        EachInput.classList.add("active");
      });
    }
  });

  let DeleteIconWrapper = document.querySelectorAll(".icon-wrapper");
  DeleteIconWrapper.forEach((EachIcon) => {
    EachIcon.addEventListener("click", HandleDelete);
  });
});
