function detailApi(db0,table0) {
  clearContent()
  let db = db0
  let table = table0
  const myHeaders = new Headers();
  myHeaders.append("Content-Type", "application/json");

  const raw = JSON.stringify({
      "db": db,
      "table": table
  });

  const requestOptions = {
      method: "POST",
      headers: myHeaders,
      body: raw,
      redirect: "follow"
  };

  fetch("http://localhost:5000/detail", requestOptions)
  .then((response) => response.json())
  .then((result) => {
    document.querySelector(".content").style.display = "flex";
    document.querySelector(".detail-item").style.display = 'flex';
    fillDetail(result)
  })
}

function tableApi(db0) {
  clearContent()
  let db = db0
  const myHeaders = new Headers();
  myHeaders.append("Content-Type", "application/json");

  const raw = JSON.stringify({
      "db": db
  });

  const requestOptions = {
      method: "POST",
      headers: myHeaders,
      body: raw,
      redirect: "follow"
  };

  fetch("http://localhost:5000/table", requestOptions)
  .then((response) => response.json())
  .then((result) => {
    document.querySelector(".content").style.display = "flex";
    document.querySelector(".table-item").style.display = 'flex';
      fillTable(result)
  })
}

function accountSshApi() {
  // showSpending()
  clearContent()
  const myHeaders = new Headers();
  myHeaders.append("Content-Type", "application/json");

  const requestOptions = {
      method: "GET",
      headers: myHeaders,
      redirect: "follow"
  };

  fetch("http://localhost:5000/account/ssh", requestOptions)
  .then((response) => response.json())
  .then((data) => {
      // hideSpending()
      document.querySelector(".content").style.display = "flex";
      document.querySelector(".ssh-item").style.display = 'flex';
      fillAccountSSH(data)
  })
}

function portsApi() {
  // showSpending()
  clearContent()
  const myHeaders = new Headers();
  myHeaders.append("Content-Type", "application/json");

  const requestOptions = {
      method: "GET",
      headers: myHeaders,
      redirect: "follow"
  };

  fetch("http://localhost:5000/ports", requestOptions)
  .then((response) => response.json())
  .then((data) => {
      // hideSpending()
      document.querySelector(".content").style.display = "flex";
      document.querySelector(".p-item").style.display = 'flex';
      fillPort(data)
  })
}

function dbsApi() {
  // showSpending()
  clearContent()
  const myHeaders = new Headers();
  myHeaders.append("Content-Type", "application/json");

  const requestOptions = {
      method: "GET",
      headers: myHeaders,
      redirect: "follow"
  };

  fetch("http://localhost:5000/db", requestOptions)
  .then((response) => response.json())
  .then((data) => {
      // hideSpending()
      document.querySelector(".content").style.display = "flex";
      document.querySelector(".d-item").style.display = 'flex';
      fillDB(data)
  })
}

function accountWebApi() {
  // showSpending()
  clearContent()
  const myHeaders = new Headers();
  myHeaders.append("Content-Type", "application/json");

  const requestOptions = {
      method: "GET",
      headers: myHeaders,
      redirect: "follow"
  };

  fetch("http://localhost:5000/account/web", requestOptions)
  .then((response) => response.json())
  .then((data) => {
      // hideSpending()
      document.querySelector(".content").style.display = "flex";
      document.querySelector(".a-item").style.display = 'flex';
      fillAccountWeb(data)
  })
}
  

function screenApi() {
  // showSpending()
  clearContent()
  const myHeaders = new Headers();
  myHeaders.append("Content-Type", "application/json");

  const requestOptions = {
      method: "GET",
      headers: myHeaders,
      redirect: "follow"
  };

  fetch("http://localhost:5000/screen", requestOptions)
  .then((response) => response.json())
  .then((result) => {
      // hideSpending()
      displayContent()
      fillDataIntoHTML(result)
  })
}

function attackApi() {
  clearContent()
  showSpending()
  let ip = document.querySelector('#ip').value
  const myHeaders = new Headers();
  myHeaders.append("Content-Type", "application/json");

  const raw = JSON.stringify({
      "ip": ip
  });

  const requestOptions = {
      method: "POST",
      headers: myHeaders,
      body: raw,
      redirect: "follow"
  };

  fetch("http://localhost:5000/attack", requestOptions)
  .then((response) => response.json())
  .then((result) => {
      hideSpending()
      displayContent()
      fillDataIntoHTML(result)
  })
}

// Hàm để thêm dữ liệu vào HTML
function fillDataIntoHTML(data) {
    // Điền thông tin về các form vào HTML
    fillForm(data)
    fillAccountWeb(data)
    fillDB(data)
    fillPort(data)
    fillAccountSSH(data)
}

function showSpending() {
  const spendingElement = document.getElementById("running");
  spendingElement.style.display = "block";
  let dots = 0;
  const intervalId = setInterval(function() {
    dots++;
    spendingElement.textContent = "running" + ".".repeat(dots);
    if (dots === 3) {
      dots = 0;
    }
  }, 500); // Đổi dấu chấm mỗi 0.5 giây

  // Lưu intervalId vào thuộc tính data của phần tử spending để có thể dễ dàng dừng interval sau này
  spendingElement.dataset.intervalId = intervalId;
}

function hideSpending() {
  const spendingElement = document.getElementById("running");
  spendingElement.style.display = "none";
  const intervalId = parseInt(spendingElement.dataset.intervalId);
  clearInterval(intervalId);
}

function clearContent() {
  const contents = document.querySelectorAll('.item-content');
  contents.forEach(content => {
    content.innerHTML = ''; // Xóa nội dung trong mỗi phần tử content
  });
  document.querySelector(".content").style.display = "none";
  const items = document.querySelectorAll(".item");
  items.forEach(item => {
    item.style.display = 'none'
  });
}

function displayContent() {
  document.querySelector(".content").style.display = "flex";
  const items = document.querySelectorAll(".item");
  items.forEach(item => {
    item.style.display = 'flex'
  });
  document.querySelector(".table-item").style.display = 'none';
  document.querySelector(".detail-item").style.display = 'none';
}

function fillForm(data) {
    const formContent = document.querySelector('.f-content');
    let index = 0
    data.forms.forEach(form => {
      index++
      const formDiv = document.createElement('div');
      formDiv.innerHTML = `<div class="content-frame">
                            <div class="content-left" >Form ${index}:</div>
                            <div class="content-right">
                              <div class="cr-item">
                                <div class="cr-item-left">Action:</div>
                                <div class="cr-item-right">${form.action}</div>
                              </div>
                              <div class="cr-item">
                                <div class="cr-item-left">Method:</div>
                                <div class="cr-item-right">${form.method}</div>
                              </div>
                              <div class="cr-item">
                                <div class="cr-item-left">Inputs:</div>
                                <div class="cr-item-right">${form.inputs.join(', ')}</div>
                              </div>
                            </div>
                          </div>`
      formContent.appendChild(formDiv);
    });
}

function fillAccountWeb(data) {
    let index = 0
    const accountWebContent = document.querySelector('.a-content');
    data.account_web.forEach(account => {
      index++
      const accountDiv = document.createElement('div');
      accountDiv.innerHTML = `<p>Username: ${account.username}, Password: ${account.password}</p>`;
      accountDiv.innerHTML = `<div class="content-frame">
                                <div class="content-left" >Account ${index}:</div>
                                <div class="content-right">
                                  <div class="cr-item">
                                    <div class="cr-item-left">Username:</div>
                                    <div class="cr-item-right">${account.username}</div>
                                  </div>
                                  <div class="cr-item">
                                    <div class="cr-item-left">Password:</div>
                                    <div class="cr-item-right">${account.password}</div>
                                  </div>
                                </div>
                              </div>`
      accountWebContent.appendChild(accountDiv);
    });
}

function fillDB(data) {
    let index = 0
    const databaseContent = document.querySelector('.d-content');
    const nameSDB = document.createElement('div');
    nameSDB.innerHTML = `<div style="font-size: 18px;padding: 5px 0;">Ten he quan tri co so du lieu: <span class="dbTitle">${data.server_db}</span></div>`
    databaseContent.appendChild(nameSDB);
    data.dbs.forEach(db => {
      index++
      const dbDiv = document.createElement('div');
      dbDiv.innerHTML = `<div class="content-frame">
                          <div class="content-left" >Database ${index}:</div>
                          <div class="content-right">
                            <div class="cr-item">
                              <div class="cr-item-right">
                                ${db}
                                <i class="fa-solid fa-table" onclick="tableApi('${db}')"></i>
                              </div>
                            </div>
                          </div>
                        </div>`;
      databaseContent.appendChild(dbDiv);
    });
}

function fillPort(data) {
    let index = 0
    const portContent = document.querySelector('.p-content');
    data.ports.forEach(port => {
      index++
      const portDiv = document.createElement('div');
      portDiv.innerHTML = `<div class="content-frame">
                            <div class="content-left" >Opening ${index}:</div>
                            <div class="content-right">
                              <div class="cr-item">
                                <div class="cr-item-left">Port:</div>
                                <div class="cr-item-right">${port.port}</div>
                              </div>
                              <div class="cr-item">
                                <div class="cr-item-left">Service:</div>
                                <div class="cr-item-right">${port.service}</div>
                              </div>
                              <div class="cr-item">
                                <div class="cr-item-left">State:</div>
                                <div class="cr-item-right">${port.state}</div>
                              </div>
                            </div>
                          </div>`
      portContent.appendChild(portDiv);
    });
}

function fillAccountSSH(data) {
    let index = 0
    const accountSSHContent = document.querySelector('.ssh-content');
    data.account_ssh.forEach(account => {
      index++
      const accountDiv = document.createElement('div');
      accountDiv.innerHTML = `<div class="content-frame">
                                <div class="content-left" >Account ${index}:</div>
                                <div class="content-right">
                                  <div class="cr-item">
                                    <div class="cr-item-left">Username:</div>
                                    <div class="cr-item-right">${account.username}</div>
                                  </div>
                                  <div class="cr-item">
                                    <div class="cr-item-left">Password:</div>
                                    <div class="cr-item-right">${account.password}</div>
                                  </div>
                                </div>
                              </div>`
      accountSSHContent.appendChild(accountDiv);
    });
}

function fillTable(data) {
  let index = 0
  const databaseContent = document.querySelector('.table-content');
  const nameSDB = document.createElement('div');
  db = data.db
  nameSDB.innerHTML = `<div style="font-size: 18px;padding: 5px 0;">Ten co so du lieu: <span class="dbTitle">${data.db}</span></div>`
  databaseContent.appendChild(nameSDB);
  data.tables.forEach(table => {
    index++
    const dbDiv = document.createElement('div');
    dbDiv.innerHTML = `<div class="content-frame">
                        <div class="content-left" >Table ${index}:</div>
                        <div class="content-right">
                          <div class="cr-item">
                            <div class="cr-item-right">
                              ${table}
                              <i class="fa-solid fa-circle-info" onclick="detailApi('${db}', '${table}')"></i>
                            </div>
                          </div>
                        </div>
                      </div>`;
    databaseContent.appendChild(dbDiv);
  });
}

function fillDetail(data) {
  let index = 0
  const databaseContent = document.querySelector('.detail-content');
  const nameSDB = document.createElement('div');
  nameSDB.innerHTML = `<div style="font-size: 18px;padding: 5px 0;">Ten co so du lieu: <span class="dbTitle">${data.db}</span></div>
  <div style="font-size: 18px;padding: 5px 0;">Ten co so du lieu: <span class="dbTitle">${data.tbl}</span></div>`
  databaseContent.appendChild(nameSDB);
  data.columns.forEach(c => {
    index++
    const dbDiv = document.createElement('div');
    dbDiv.innerHTML = `<div class="content-frame">
                        <div class="content-left" >Column ${c.column}:</div>
                        <div class="content-right">
                          <div class="cr-item">
                            <div class="cr-item-right">
                              ${c.values}
                            </div>
                          </div>
                        </div>
                      </div>`;
    databaseContent.appendChild(dbDiv);
  });
}


