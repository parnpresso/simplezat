context("Actions", () => {
  beforeEach(() => {
    cy.visit("http://localhost:8000/ratings");
  });

  it("should be able to give positive rating with comment", () => {
    cy.contains("How do we do?");
    cy.get('[href="positive/"] > img').should("have.attr", "alt", "Positive");
    cy.get('[href="neutral/"] > img').should("have.attr", "alt", "Neutral");
    cy.get('[href="negative/"] > img').should("have.attr", "alt", "Negative");

    cy.get('[href="positive/"] > img').click();
    cy.wait(1000);

    cy.contains("Any comment?");
    cy.get("textarea").type("You are doing great!");
    cy.get('[type="submit"]').click();
    cy.wait(1000);

    cy.contains("Thank you");
  });
});
