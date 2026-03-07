const fs = require("fs");

const moduleData = JSON.parse(fs.readFileSync("module.json", "utf8"));
const sqlModules = JSON.parse(fs.readFileSync("sql_modules.json", "utf8"));

const step4Row = sqlModules.find(
  (row) => row.testCase === "step4"
);

console.log("Step 4: Check for name mismatches caused by capitalization or spacing");
console.log("JSON Module Name:", moduleData.moduleName);

if (step4Row && step4Row.module_name === moduleData.moduleName) {
  console.log("Exact match found in SQL data.");
  console.log("SQL Module Name:", step4Row.module_name);
  console.log("SQL Status:", step4Row.status);
} else {
  console.log("No exact match found.");

  const normalizedJsonName = moduleData.moduleName.trim().toLowerCase();

  if (
    step4Row &&
    step4Row.module_name.trim().toLowerCase() === normalizedJsonName
  ) {
    console.log("Possible match found after normalizing text.");
    console.log("JSON Module Name:", moduleData.moduleName);
    console.log("SQL Module Name:", step4Row.module_name);
    console.log("SQL Status:", step4Row.status);
    console.log("Result: Names differ in formatting, but likely refer to the same module.");
  } else {
    console.log("Result: No matching module found, even after normalization.");
  }
}