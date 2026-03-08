const fs = require("fs");

const data = JSON.parse(fs.readFileSync("module.json", "utf8"));

console.log("Step 1: Confirm Module Publication Status");
console.log("Module Name:", data.moduleName);
console.log("Status:", data.status);

if (data.status === "published") {
  console.log("Result: Module is published.");
} else {
  console.log("Result: Module is not published.");
}