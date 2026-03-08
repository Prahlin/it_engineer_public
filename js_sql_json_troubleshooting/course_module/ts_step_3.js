const fs = require("fs");

const moduleData = JSON.parse(fs.readFileSync("module.json", "utf8"));
const sqlModules = JSON.parse(fs.readFileSync("sql_modules.json", "utf8"));

const matchedModule = sqlModules.find(
  (row) => row.testCase === "step3"
);

console.log("Step 3: Compare JSON Status with SQL Status");
console.log("JSON Module Name:", moduleData.moduleName);
console.log("JSON Status:", moduleData.status);

if (matchedModule) {
  console.log("SQL Module Name:", matchedModule.module_name);
  console.log("SQL Status:", matchedModule.status);

  if (matchedModule.status === moduleData.status) {
    console.log("Result: JSON and SQL statuses match.");
  } else {
    console.log("Result: JSON and SQL statuses DO NOT match.");
  }
} else {
  console.log("Result: No matching module found in SQL data.");
}