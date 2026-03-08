const fs = require("fs");

const moduleData = JSON.parse(fs.readFileSync("module.json", "utf8"));
const sqlModules = JSON.parse(fs.readFileSync("sql_modules.json", "utf8"));
const statusMapping = JSON.parse(fs.readFileSync("status_mapping.json", "utf8"));

const matchedModule = sqlModules.find(
  (row) => row.testCase === "step5"
);

console.log("Step 5: Check for status mismatches caused by different status labels");
console.log("JSON Module Name:", moduleData.moduleName);
console.log("JSON Status:", moduleData.status);

if (matchedModule) {
  console.log("SQL Module Name:", matchedModule.module_name);
  console.log("SQL Status:", matchedModule.status);

  if (matchedModule.status === moduleData.status) {
    console.log("Result: JSON and SQL statuses match exactly.");
  } else {
    console.log("No exact status match found.");

    const allowedStatuses = statusMapping[moduleData.status];

    if (allowedStatuses) {
      if (allowedStatuses.includes(matchedModule.status)) {
        console.log("Result: Status labels differ, but they mean the same thing.");
      } else {
        console.log("Result: Status values do NOT match, even after using the mapping.");
      }
    } else {
      console.log("Result: No mapping exists for the JSON status.");
    }
  }
} else {
  console.log("Result: No matching module found in SQL data.");
}