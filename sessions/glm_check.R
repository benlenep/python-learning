# Session 17: fit the same GLMs in R and save the coefficients for comparison.
# Run from the sessions folder, after the notebook has written glm_data.csv:
#   cd sessions && Rscript glm_check.R && cd ..

members <- read.csv("glm_data.csv", stringsAsFactors = FALSE)
members$tier    <- factor(members$tier, levels = c("basic", "mid", "top"))
members$channel <- factor(members$channel, levels = c("direct", "broker", "online"))

bin <- glm(churned ~ age + tenure_years + tier + channel, family = binomial, data = members)
pois <- glm(claims ~ age + tier, family = poisson, offset = log(exposure), data = members)

write.csv(data.frame(term = names(coef(bin)), estimate = unname(coef(bin))),
          "r_glm_binomial.csv", row.names = FALSE)
write.csv(data.frame(term = names(coef(pois)), estimate = unname(coef(pois))),
          "r_glm_poisson.csv", row.names = FALSE)

print(round(coef(bin), 4))
print(round(coef(pois), 4))
