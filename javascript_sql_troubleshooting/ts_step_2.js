const fs = require("fs");

const moduleData = JSON.parse(fs.readFileSync("module.json", "utf8"));
const sqlModules = JSON.parse(fs.readFileSync("sql_modules.json", "utf8"));

const step2Row = sqlModules.find(
  (row) => row.testCase === "step2"
);

console.log("Step 2: Confirm Module Exists in SQL Data");
console.log("Looking for module:", moduleData.moduleName);

if (step2Row && step2Row.module_name === moduleData.moduleName) {
  console.log("Result: Module found in SQL data.");
  console.log("SQL Status:", step2Row.status);
} else {
  console.log("Result: Module NOT found in SQL data.");
}