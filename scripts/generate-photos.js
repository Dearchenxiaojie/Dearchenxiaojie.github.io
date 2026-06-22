const fs = require("fs")
const path = require("path")

const galleryDir = path.join(__dirname, "..", "docs", "public", "gallery")
const outputFile = path.join(__dirname, "..", "docs", ".vitepress", "theme", "photos.json")

function scan(dir) {
  const result = {}
  const years = fs.readdirSync(dir).filter(f => /^\d{4}$/.test(f)).sort()
  for (const year of years) {
    const yearDir = path.join(dir, year)
    // Month dirs are named like "2023-04" (YYYY-MM format)
    const monthDirs = fs.readdirSync(yearDir)
      .filter(f => new RegExp(`^${year}-(\\d{2})$`).test(f))
      .sort()
    result[year] = {}
    for (const monthDir of monthDirs) {
      const month = monthDir.slice(-2) // extract "04" from "2023-04"
      result[year][month] = fs.readdirSync(path.join(yearDir, monthDir))
        .filter(f => /\.(jpg|jpeg|png|webp)$/i.test(f)).sort()
    }
  }
  return result
}

const photos = scan(galleryDir)
fs.writeFileSync(outputFile, JSON.stringify(photos, null, 2), "utf-8")
console.log(`photos.json generated with ${Object.keys(photos).length} years`)
